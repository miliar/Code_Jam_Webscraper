# not most effective, but fast enough

def findmin(m):
    mx, my, mv = 0,0,1000
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] < mv:
                mv = m[i][j]
                mx = j
                my = i
    return (mx, my, mv)

n = int(raw_input())
for test in xrange(n):
    h, w = map(int, raw_input().split())
    m = [map(int, raw_input().split()) for i in range(h)]
    
    
    while m:
        x, y, v = findmin(m)

        # whole row or column must be of value v
        if all(m[y][i] == v for i in range(w)):
            del m[y]
            h -= 1
        elif all(m[i][x] == v for i in range(h)):
            w -= 1
            m = [m[i][:x]+m[i][x+1:] for i in range(h)] # del column
        else:
            r = "NO"
            break
    else:
        r = "YES"
    print "Case #{0}: {1}".format(test+1,r)

