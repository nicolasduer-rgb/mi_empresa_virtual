
# start_server.ps1 - Servidor local para mi_empresa_virtual
# Sirve el directorio actual en http://localhost:8080

$port = 8080
$root = $PSScriptRoot

$listener = New-Object System.Net.HttpListener
$listener.Prefixes.Add("http://localhost:$port/")
$listener.Start()

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Servidor iniciado correctamente!" -ForegroundColor Green
Write-Host "  Abre en el navegador:" -ForegroundColor White
Write-Host "  http://localhost:$port" -ForegroundColor Yellow
Write-Host "  (Presiona Ctrl+C para detener)" -ForegroundColor Gray
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Abre el navegador automaticamente
Start-Process "http://localhost:$port"

$mimeTypes = @{
    ".html" = "text/html"
    ".js"   = "application/javascript"
    ".css"  = "text/css"
    ".png"  = "image/png"
    ".jpg"  = "image/jpeg"
    ".gif"  = "image/gif"
    ".svg"  = "image/svg+xml"
    ".ico"  = "image/x-icon"
}

while ($listener.IsListening) {
    try {
        $context  = $listener.GetContext()
        $request  = $context.Request
        $response = $context.Response

        $urlPath = $request.Url.LocalPath
        if ($urlPath -eq "/") { $urlPath = "/index.html" }

        $filePath = Join-Path $root $urlPath.TrimStart("/")

        if (Test-Path $filePath -PathType Leaf) {
            $ext       = [System.IO.Path]::GetExtension($filePath).ToLower()
            $mimeType  = if ($mimeTypes.ContainsKey($ext)) { $mimeTypes[$ext] } else { "application/octet-stream" }
            $bytes     = [System.IO.File]::ReadAllBytes($filePath)
            $response.ContentType   = $mimeType
            $response.ContentLength64 = $bytes.Length
            $response.OutputStream.Write($bytes, 0, $bytes.Length)
            Write-Host "  200  $urlPath" -ForegroundColor Green
        } else {
            $response.StatusCode = 404
            $msg  = [System.Text.Encoding]::UTF8.GetBytes("404 - Archivo no encontrado: $urlPath")
            $response.OutputStream.Write($msg, 0, $msg.Length)
            Write-Host "  404  $urlPath" -ForegroundColor Red
        }

        $response.Close()
    } catch {
        if ($listener.IsListening) {
            Write-Host "Error: $_" -ForegroundColor Red
        }
    }
}
