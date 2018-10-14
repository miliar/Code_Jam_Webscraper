name = 'B'
typ = 'large'
base = name+'-'+typ+'.'
vstup = file(base+'in').read()

UP,LEFT,RIGHT,DOWN = range(4)
INF = 1000000

def getrel(d):
    return ((0,-1),(-1,0),(1,0),(0,1))[d]

def around(x,y):
    ret = [INF]*4
    if x>0: ret[LEFT] = m[y][x-1]
    if x<W-1: ret[RIGHT] = m[y][x+1]
    if y>0: ret[UP] = m[y-1][x]
    if y<H-1: ret[DOWN] = m[y+1][x]
    return ret

def goes_to(x,y):
    a = around(x,y)
    sm_val = INF
    sm_i = -1
    for i in xrange(4):
        if a[i] < sm_val:
            sm_val = a[i]
            sm_i = i
    return sm_i if sm_val < m[y][x] else -1

def solve():
    sinks = []
    pathmap = [[[] for  c1 in xrange(W)] for c2 in xrange(H)]
    for y in xrange(H):
        for x in xrange(W):
            d = goes_to(x,y)
            if d == -1:sinks.append((x,y))
            else:
                rx,ry = getrel(d)
                pathmap[y+ry][x+rx].append((x,y))
    i = 0
    res = [[-1 for  c1 in xrange(W)] for c2 in xrange(H)]
    for s in sinks:
        cur = [s]
        res[s[1]][s[0]] = i
        while len(cur):
            t = cur.pop(0)
            cur.extend(pathmap[t[1]][t[0]])
            for coord in pathmap[t[1]][t[0]]:
                res[coord[1]][coord[0]] = i
        i += 1
    ch_i = 97
    ch = chr(ch_i)
    n = res[0][0]
    trans = {n:ch}
    for y in xrange(H):
        for x in xrange(W):
            if res[y][x] not in trans:
                ch_i+=1; ch = chr(ch_i)
                n = res[y][x]
                trans[n] = ch
            res[y][x] = trans[res[y][x]]
    return '\n'.join([' '.join(c1) for c1 in res])
            

lines = vstup.split('\n')
T = int(lines[0])

fi = 1
i = 1
vystup = file(base+'out', 'w')
for M in xrange(T):
    H, W = (int(c1) for c1 in lines[fi].split(' '))
    fi += 1
    m = []
    for h in xrange(H):
        row = [int(c1) for c1 in lines[fi].split(' ')]
        fi += 1
        m.append(row)
    vystup.write('Case #' + str(i) + ':\n' + str(solve()) + '\n')
    i += 1
vystup.close()
