#! /usr/bin/python3

def readint(): return int(input())
def readarray(f): return map(f, input().split())

_cases = readint()
for _case in range(_cases):
    (n,v,x) = input().split()
    n = int(n)
    v = int(v.translate({ord('.'):None}))
    x = int(x.translate({ord('.'):None}))
    sources = []
    for _ in range(n):
        (r,c) = input().split()
        (r,c) = (int(r.translate({ord('.'):None})),int(c.translate({ord('.'):None})))
        sources.append((r,c))
    
    # print(n, v, x, sources)
    if len(sources) == 1:
        if sources[0][1] == x:
            t = v / sources[0][0]
        else:
            t = "IMPOSSIBLE"
        print("Case #" + str(_case+1) + ":", t)
    elif len(sources) == 2:
        if x > sources[0][1] and x > sources[1][1]:
            t = "IMPOSSIBLE"
        elif x < sources[0][1] and x < sources[1][1]:
            t = "IMPOSSIBLE"
        elif sources[0][1] == sources[1][1]:
            t = v / (sources[0][0] + sources[1][0])
        else:
            v0 = v*(x-sources[1][1])/(sources[0][1]-sources[1][1])
            v1 = v*(sources[0][1]-x)/(sources[0][1]-sources[1][1])
            # print(v0,v1, n, v, x, sources)
            t = max(v0/sources[0][0], v1/sources[1][0])
        print("Case #" + str(_case+1) + ":", t)
