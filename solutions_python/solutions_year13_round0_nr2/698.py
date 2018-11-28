fin = open('mow.in', 'r')

t = int(fin.readline())
for l in range(1, t+1):
    n, m = map(int, fin.readline().split(' '))
    grass = []
    for i in range(0, n):
        grass.append(map(int, fin.readline().split(' ')))
    works = True
    for i in range(0, n):
        if(not works):
            break
        for j in range(0, m):
            if(not works):
                break
            lr = True
            ud = True
            y = i
            x = j
            while(y>=0):
                if(grass[i][j] < grass[y][j]):
                    ud = False
                    break
                y -= 1
            while(x>=0):
                if(grass[i][j] < grass[i][x]):
                    lr = False
                    break
                x -= 1
            y = i
            x = j
            while(y<n):
                if(grass[i][j] < grass[y][j]):
                    ud = False
                    break
                y += 1
            while(x<m):
                if(grass[i][j] < grass[i][x]):
                    lr = False
                    break
                x += 1
            if(not ud and not lr):
                works = False
    if(not works):
        print "Case #%d: NO" % l
    else: 
        print "Case #%d: YES" % l
        
