from collections import defaultdict

t = input()

class Bot(object):
    def __init__(self):
        self.p = 1
        self.l = 0

def solve():
    s = raw_input().split()
    n = int(s[0])
    u,v = Bot(),Bot()
    res = 0
    for i in xrange(n):
        a,b = (v,u) if s[i*2+1]=='O' else (u,v)
        p = int(s[i*2+2])
        l = max(0,abs(p-a.p)-a.l)
        res+=l+1
        b.l+=l+1
        a.p=p
        a.l=0
    return res
    

for i in xrange(t):
    print "Case #%d: %d"%(i+1,solve())
        