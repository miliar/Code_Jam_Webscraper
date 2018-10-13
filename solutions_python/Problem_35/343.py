INPUT_FILE = 'inputs/B-large.in'
OUTPUT_FILE = 'outputs/B-large.out'

def spread(area_map, cell, code):
    cell['code'] = code
    for nextCellCoords in cell['out']:
        nextCell = area_map[nextCellCoords[0]][nextCellCoords[1]]
        if (nextCell['code'] == ''):
            spread(area_map, nextCell, code)
    for prevCellCoords in cell['in']:
        prevCell = area_map[prevCellCoords[0]][prevCellCoords[1]]
        if (prevCell['code'] == ''):
            spread(area_map, prevCell, code)

f_in = open(INPUT_FILE, 'r')
f_out = open(OUTPUT_FILE, 'w+')

T = int(f_in.readline())

for t in range(T):
    area_map = []
    H, W = [int(i) for i in f_in.readline().split()]
    for h in range(H):
        area_map.append([{'alt': int(i), 'in': [], 'out': [], 'code': ''} for i in f_in.readline().split()])
    for h in range(H):
        for w in range(W):
            altN = altW = altE = altS = alt = area_map[h][w]['alt']
            if h > 0:
                altN = area_map[h - 1][w]['alt']
            if w > 0:
                altW = area_map[h][w - 1]['alt']
            if w < W - 1:
                altE = area_map[h][w + 1]['alt']
            if h < H - 1:
                altS = area_map[h + 1][w]['alt']
            altMin = min(alt, altN, altW, altE, altS)
            
            if (altMin == alt):
                continue
            elif (altMin == altN):
                area_map[h - 1][w]['in'].append([h, w])
                area_map[h][w]['out'].append([h - 1, w])
            elif (altMin == altW):
                area_map[h][w - 1]['in'].append([h, w])
                area_map[h][w]['out'].append([h, w - 1])
            elif (altMin == altE):
                area_map[h][w + 1]['in'].append([h, w])
                area_map[h][w]['out'].append([h, w + 1])
            elif (altMin == altS):
                area_map[h + 1][w]['in'].append([h, w])
                area_map[h][w]['out'].append([h + 1, w])
    
    codes = 'abcdefghijklmnopqrstuvwxyz'
    codeIndex = 0
    for h in range(H):
        for w in range(W):
            cell = area_map[h][w]
            if cell['code'] == '':
                spread(area_map, cell, codes[codeIndex])
                codeIndex = codeIndex + 1
                
    f_out.write("Case #" + str(t + 1) + ": \n")
    for h in range(H):
        for w in range(W):
            f_out.write(area_map[h][w]['code'] + ' ')
        f_out.write('\n')
            
f_in.close()
f_out.close()