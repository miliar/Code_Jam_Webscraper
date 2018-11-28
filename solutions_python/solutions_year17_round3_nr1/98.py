import sys

filename = sys.argv[1]
f = open(filename)

cases = int(f.next())


def keyr(c):
    return c.r

pi = 3.141592653589793


class Cake:
    def __init__(self, r, h):
        self.r = r
        self.h = h

    def area(self):
        return self.r * self.h * 2 * pi

def ccmp(x,y):
    if x.r < y.r:
        return -1
    if x.r > y.r:
        return 1
    if x.area() < y.area():
        return -1
    return 1

def solve():
    n, k = map(int, f.next().split())
    r  = []
    h = []
    cakes = []
    for i in range(n):
        rr, hh = map(int, f.next().split())
        r.append(r)
        h.append(hh)
        cakes.append(Cake(rr, hh))
    
    cakes = sorted(cakes,cmp=ccmp,reverse=True)
    ans = 0.0
    
    for i in range(n):
        if n-i < k:
            break
        s = pi * cakes[i].r * cakes[i].r + cakes[i].area()
        #print s
        left = []
        for j in range(n):
            if i != j:
                left.append(cakes[i])
        left = sorted(cakes, key=lambda d:d.area(), reverse=True)
        for j in range(k-1):
            s = s + left[j].area()
            #print s
        ans = max(ans, s)

    return "%.6f"%ans

for i in range(1, cases+1):
    print("Case #%d: %s"%(i, solve()))