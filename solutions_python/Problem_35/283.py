# -*- coding: utf-8 -*-

fin = open("b.in","r")
T = int(fin.readline())

alt = []
H = 0
W = 0

def valid(p):
    row, col = p
    return row >= 0 and row < H and col >= 0 and col < W
    
def galt(p):
    row, col = p
    if valid(p):
        return alt[row][col]
    else:
        return 1000000
        
# 0 - sink, 1 - up, 2 - right, 3 - down, 4 - left
def child(p):
    if not valid(p):
        return None
    row, col = p
    a = galt(p)
    u = galt((row-1,col))
    d = galt((row+1,col))
    l = galt((row,col-1))
    r = galt((row,col+1))
    m = min([u,d,l,r,a])
    if a == m:
        return p
    if u == m:
        return (row-1,col)
    if l == m:
        return (row,col-1)
    if r == m:
        return (row,col+1)
    if d == m:
        return (row+1,col)
    
def parents(p):
    par = []
    for n in nbs(p):
        if child(n) == p:
            par.append(n)
    return par
    
def nbs(p):
    r,c = p
    return filter(valid, [(r-1,c),(r+1,c),(r,c-1),(r,c+1)])
    
for i in range(T):
    print "Case #%d:" % (i+1)
    H, W = map(int, fin.readline().split())
    alt = []
    for r in range(H):
        alt.append(map(int, fin.readline().split()))
        
    positions = zip([x/W for x in range(W*H)], range(W)*H)
    
    sinks = filter(lambda p: child(p) == p, positions)
    
    names = {}
    
    
    
    basins = {}
    
    for s in sinks:
        todo = set([s])
        while todo:
            k = todo.pop()
            basins[k] = s
            for p in parents(k):
                if p not in basins:
                    todo.add(p)
    
    o = ord('a')
    for r in range(H):
        for c in range(W):
            b = basins[(r,c)]
            if b not in names:
                names[b] = chr(o)
                o += 1
            print names[b],
        print
    
        
        
    
    