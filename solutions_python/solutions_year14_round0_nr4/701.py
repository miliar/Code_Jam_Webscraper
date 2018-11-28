import sys

class War:

    def __init__(self, N, ns, ks):
        self.N = N
        self.ns = sorted(ns)
        self.ks = sorted(ks)
        self.np = 0

    def solve(self):
        for i in range(N):
            self.process()

    def process(self):
        n = self.ns.pop()
        k = next((x for x in self.ks if x > n), None)
        if not k:
            k = self.ks[0]
        self.ks.remove(k)
        if n > k:
            self.np += 1

class DWar:

    def __init__(self, N, ns, ks):
        self.N = N
        self.ns = sorted(ns)
        self.ks = sorted(ks)
        self.np = 0

    def solve(self):
        for i in range(N):
            self.process()

    def process(self):
        n = self.ns.pop(0)
        k = next((x for x in self.ks if x < n), None)
        if not k:
            k = self.ks[len(self.ks) - 1]
        self.ks.remove(k)
        if n > k:
            self.np += 1


T = int(sys.stdin.readline())
for t in range(1, T+1):
    N = int(sys.stdin.readline())
    ns = [float(x) for x in sys.stdin.readline().split()]
    ks = [float(x) for x in sys.stdin.readline().split()]

    w = War(N, ns, ks)
    w.solve()

    dw = DWar(N, ns, ks)
    dw.solve()

    print "Case #%d: %d %d" % (t, dw.np, w.np)
