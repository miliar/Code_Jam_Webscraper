import sys

filename = sys.argv[1]
f = open(filename)

cases = int(f.next())


class T:
    def __init__(self,a,b,c):
        self.st = a
        self.ed = b
        self.w = c

def solve():
    a,b = map(int, f.next().split())
    events = []

    left0 = left1 = 720
    cc = 0
    for i in range(a):
        st, ed = map(int, f.next().split())
        cc = T(st,ed,0)
        events.append(cc)
    
    for i in range(b):
        st, ed = map(int, f.next().split())
        cc = T(st,ed,1)
        events.append(cc)
    
    events = sorted(events, key=lambda x:x.st)

    for e in events:
        if e.w == 0:
            left0 -= e.ed - e.st
        else:
            left1 -= e.ed - e.st

    cc = events[a+b-1]
    d = T(cc.st-1440,cc.ed-1440,cc.w)
    events.insert(0, d)

    v1 = []
    v2 = []
    ans = 0
    for i in range(1, a+b+1):
        if not events[i].w == events[i-1].w:
             ans += 1
        
        if events[i].w == events[i-1].w:
            if events[i].w == 0:
                v1.append(events[i].st - events[i-1].ed)
            else:
                v2.append(events[i].st-events[i-1].ed)
    
    v1 = sorted(v1)
    v2 = sorted(v2)

    for k in v1:
        if k <= left0:
            left0 -= k
        else:
            ans += 2

    for k in v2:
        if k <= left1:
            left1 -= k
        else:
            ans += 2


    return "%d"%ans

for i in range(1, cases+1):
    print("Case #%d: %s"%(i, solve()))