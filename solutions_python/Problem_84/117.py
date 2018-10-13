filename = 'A-large';
fin = open(filename + '.in', 'r')
out = open(filename + '.out', 'w')

T = int(fin.readline())

for t in range(1, T+1):
    (R, C) = tuple(map(lambda x: int(x), fin.readline().split(' ')))
    
    pict = []
    
    blue = 0
    
    for r in range(0, R):
        pict.append(map(lambda x: x, fin.readline().strip()))
        for c in range(0, C):
            if pict[r][c] == '#':
                blue += 1
        
    
    red = 0
    
    for i in range(0, R):
        for j in range(0, C):
            if i < R-1 and j < C -1:
                if pict[i][j] == '#' and pict[i+1][j] == '#' and pict[i][j+1] == '#' and pict[i+1][j+1] == '#':
                    pict[i][j] = '/'
                    pict[i+1][j] = '\\'
                    pict[i][j+1] = '\\'
                    pict[i+1][j+1] = '/'
                    red += 1
                
                
    out.write('Case #%d:\n' % t)
    if blue == red * 4:
        for p in pict:
            out.write('%s\n' % reduce(lambda s1, s2: s1 + s2, p))
    else:
        out.write('Impossible\n')
    