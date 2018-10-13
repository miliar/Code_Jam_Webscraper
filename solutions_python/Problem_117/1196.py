import sys

f = open(sys.argv[1], 'r')

T = int(f.readline())
for t in range(T):
    N, M = [int(x) for x in f.readline().strip().split()]
    
    lawn = []
    search_order = []
    for y in range(N):
        row = [int(x) for x in f.readline().strip().split()]
        for x, l in enumerate(row):
            search_order.append((l, (x, y)))
        lawn.append(row)
    search_order = sorted(search_order)
    
    result = 'YES'
    for h, pos in search_order:
        x, y = pos
        
        horiz = True
        for i in range(M):
            if h < lawn[y][i]:
                horiz = False
                break
        
        vert = True
        for i in range(N):
            if h < lawn[i][x]:
                vert = False
                break
        
        if not horiz and not vert:
            result = 'NO'
            break
    
    print('Case #%d: %s' % (t + 1, result))

f.close()