import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Add Google Font to HEAD
text = text.replace('<script src=\"https://cdn.jsdelivr.net/npm/phaser@3.60.0/dist/phaser-arcade-physics.min.js\"></script>', 
    '<script src=\"https://cdn.jsdelivr.net/npm/phaser@3.60.0/dist/phaser-arcade-physics.min.js\"></script>\n    <link href=\"https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap\" rel=\"stylesheet\">')

# 1b. Configurar tipografia en el body css
text = text.replace('overflow: hidden; }', 'overflow: hidden; font-family: \'Press Start 2P\', cursive; }')

# 2. Add pixelArt to config
text = text.replace('backgroundColor: \'#1a1a2e\',',
    'backgroundColor: \'#1a1a2e\',\n    pixelArt: true,\n    antialias: false,')

# 3. Exterior Text Replacements
text = text.replace('{ fontSize: \'60px\', fill: \'#fff\', fontStyle: \'bold\', stroke: \'#3498db\', strokeThickness: 3 }',
    '{ fontFamily: \'\"Press Start 2P\"\', fontSize: \'40px\', fill: \'#fff\', stroke: \'#3498db\', strokeThickness: 6 }')

text = text.replace('TIMBRE\', { fontSize: \'9px\', fill: \'#f1c40f\', fontStyle: \'bold\' }',
    'TIMBRE\', { fontFamily: \'\"Press Start 2P\"\', fontSize: \'6px\', fill: \'#f1c40f\' }')

text = text.replace('{ fontSize: \'16px\', fill: \'#ffe082\', backgroundColor: \'#000000cc\', padding: { x: 12, y: 7 }, fontStyle: \'bold\' }',
    '{ fontFamily: \'\"Press Start 2P\"\', fontSize: \'10px\', fill: \'#ffe082\', backgroundColor: \'#000000cc\', padding: { x: 12, y: 12 } }')

text = text.replace('{ fontSize: \'22px\', fill: \'#fff\', backgroundColor: \'#000000dd\', padding: { x: 16, y: 10 }, fontStyle: \'bold\' }',
    '{ fontFamily: \'\"Press Start 2P\"\', fontSize: \'14px\', fill: \'#fff\', backgroundColor: \'#000000dd\', padding: { x: 16, y: 16 }, lineSpacing: 6 }')

# 4. Interior Scene labels
text = text.replace('const ls = { fontSize: \'13px\', fill: \'#fff\', fontStyle: \'bold\', stroke: \'#000\', strokeThickness: 3, align: \'center\' };',
    'const ls = { fontFamily: \'\"Press Start 2P\"\', fontSize: \'9px\', fill: \'#fff\', stroke: \'#000\', strokeThickness: 3, align: \'center\' };')

text = text.replace('const sm = { fontSize: \'11px\', fill: \'#fff\', fontStyle: \'bold\', stroke: \'#000\', strokeThickness: 2, align: \'center\' };',
    'const sm = { fontFamily: \'\"Press Start 2P\"\', fontSize: \'7px\', fill: \'#fff\', stroke: \'#000\', strokeThickness: 3, align: \'center\' };')

# 5. Salida de emergencia text
text = text.replace('{ fontSize: \'10px\', fill: \'#ff4444\', fontStyle: \'bold\', align: \'center\' }',
    '{ fontFamily: \'\"Press Start 2P\"\', fontSize: \'8px\', fill: \'#ff4444\', align: \'center\', stroke: \'#000\', strokeThickness: 2 }')

# 6. UI Dialog & Hints
text = text.replace('fontSize: \'14px\', fill: \'#ffe082\', backgroundColor: \'#000000aa\',\n            padding: { x: 10, y: 5 }, fontStyle: \'bold\'',
    'fontFamily: \'\"Press Start 2P\"\', fontSize: \'10px\', fill: \'#ffe082\', backgroundColor: \'#000000aa\',\n            padding: { x: 10, y: 10 }')

text = re.sub(r\"\{ fontSize: '13px', fill: '#ff0', backgroundColor: '#000c', padding: \{ x: 5, y: 3 \}, fontStyle: 'bold' \}\",
r\"{ fontFamily: '\"Press Start 2P\"', fontSize: '8px', fill: '#ff0', backgroundColor: '#000c', padding: { x: 8, y: 8 } }\", text)

text = re.sub(r\"this.dialogBox = this.add.rectangle\(500, 600, 800, 100, 0x000000, 0.85\).setDepth\(40\).setAlpha\(0\).setScrollFactor\(0\);\",
r\"this.dialogBox = this.add.rectangle(500, 600, 800, 120, 0x000000, 0.9).setDepth(40).setAlpha(0).setScrollFactor(0);\n        this.dialogBox.setStrokeStyle(4, 0xffffff);\", text)

text = re.sub(r\"\{ fontSize: '20px', fill: '#fff', wordWrap: \{ width: 760 \} \}\",
r\"{ fontFamily: '\"Press Start 2P\"', fontSize: '14px', fill: '#fff', wordWrap: { width: 740 }, lineSpacing: 10 }\", text)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated index.html to pixel art')
