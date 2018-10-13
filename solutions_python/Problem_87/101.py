#!/usr/bin/python

def parse():
    global w
    cur = 0
    n = []
    for b,e,sw in w:
        if cur != b: 
            n.append((cur,b,0))
        cur = e
    if e != x:
        n.append((e,x,0))
    w += n
    n = []
    for i in w:
        n.append((i[2],i[0],i[1]))
    w = n
    w.sort()

def solve():
    parse()
    time = 0.0
    global t
    for sw,b,e in w:
        d = float(e - b)
        if t <= 0:
            time += d/(s + sw)
        else:
            dtime = min(d/(r + sw),t) 
            if dtime == t:
                cur = b + dtime*(r+sw)
                w.append((sw,cur,e))
            t -= dtime  
            time += dtime
    return time

r = input()
for case in range(1,r+1):
    l = map(float,raw_input().split())
    x,s,r,t,n = tuple(l) 
    w = []
    for _ in range(int(n)):
        w.append(map(int,list(raw_input().split())))
    sol = solve()
    print "Case #%s: %.6f" % (case, sol)
