import sys


class Case(object):

    def __init__(self, n, stream):
        self._id = n
        self._stream = stream
        self._base_rate = 2.0

    def _best(self, cost, boost, target):
        baseline = target / self._base_rate
        invest = 0

        old_cost = None
        vel = self._base_rate

        while True:
            invest += cost/vel
            vel += boost
            finish = target / vel

            if finish < 0.0000001:
                return invest

            final_cost = invest + finish
            if old_cost is not None and final_cost > old_cost:
                return min(baseline, old_cost)

            old_cost = final_cost

    def solve(self):
        _C, _F, _X = [float(item) for item
                      in self._stream.readline().split()]

        optimum = self._best(_C, _F, _X)
        self.report(optimum)

    def report(self, msg):
        print "Case #%d: %s" % (self._id, msg)

if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

    t = int(f.readline())
    for _t in xrange(1, t+1):
        c = Case(_t, f)
        c.solve()
