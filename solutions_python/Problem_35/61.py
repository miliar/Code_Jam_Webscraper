import re


def findsink(x, y):
    global mysink, sinks, H, W, m
    if mysink[y][x] != -1:
        return mysink[y][x]
    u = m[y-1][x]
    d = m[y+1][x]
    l = m[y][x-1]
    r = m[y][x+1]
    if u <= d and u <= l and u <= r:
        mysink[y][x] = findsink(x, y-1)
    elif l <= u and l <= d and l <= r:
        mysink[y][x] = findsink(x-1, y)
    elif r <= d and r <= l and r <= u:
        mysink[y][x] = findsink(x+1, y)
    elif d <= u and d <= l and d <= r:
        mysink[y][x] = findsink(x, y+1)
    else:
        print 'error'
    return mysink[y][x]
global mysink, sinks, H, W, m
    
s = raw_input()
maps = int(s)
for case in range(maps):
    s = raw_input().split(' ')
    H = int(s[0])
    W = int(s[1])
    m = [[1000001] * (W + 2) for d in range(H + 2)]
    sinks = []
    mysink = [[-1] * (W + 2) for d in range(H + 2)]
    for y in range(H):
        s = raw_input().split(' ')
        for x in range(W):
            m[y+1][x+1] = int(s[x])
    print 'Case #%d: ' % (case+1)
    for y in range(H):
        for x in range(W):
            c = m[y+1][x+1]
            if c <= m[y][x+1] and c <= m[y+1][x] and c <= m[y+2][x+1] and c <= m[y+1][x+2]:
                mysink[y+1][x+1] = len(sinks)
                sinks += [(x+1,y+1)]
    sinklet = ['*'] * len(sinks)
    letter = 97
    for y in range(H):
        for x in range(W):
            sink = findsink(x+1,y+1)
            if sinklet[sink] == '*':
                sinklet[sink] = chr(letter)
                letter = letter + 1
            print sinklet[sink],
        print
                

    
    
