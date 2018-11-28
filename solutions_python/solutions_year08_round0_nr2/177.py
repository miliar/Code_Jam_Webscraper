#!/usr/bin/env python
class Solver(object):
    # (time, priority, action)
    def __init__(self):
        turnaround = int(raw_input())
        na, nb = (int(x) for x in raw_input().split())
        q = []
        for i in range(na):
            ta, tb = (self.convert_time(x) for x in raw_input().split())
            q.append((ta, 1, lambda: self.leavea()))
            q.append((tb+turnaround, 0, lambda: self.idleb()))
        for i in range(nb):
            tb, ta = (self.convert_time(x) for x in raw_input().split())
            q.append((tb, 1, lambda: self.leaveb()))
            q.append((ta+turnaround, 0, lambda: self.idlea()))
        q.sort()
        self.q=q
        self.a=0
        self.b=0
        self.needa=0
        self.needb=0
        return
    
    def convert_time(self, tmstr):
        h, m = (int(x) for x in tmstr.split(':'))
        return h*60 + m

    def solve(self):
        for time, priority, action in self.q:
            action()
        return self.needa, self.needb

    def leavea(self):
        if self.a>0:
            self.a -= 1
        else:
            self.needa += 1
        return

    def leaveb(self):
        if self.b>0:
            self.b -= 1
        else:
            self.needb += 1
        return

    def idlea(self):
        self.a += 1
        return

    def idleb(self):
        self.b += 1
        return

n = int(raw_input())
for i in range(n):
    a, b = Solver().solve()
    print "Case #%d: %d %d"%(i+1, a, b)


