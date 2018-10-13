class Solution(object):
    def __init__(self, d, ns):
        self.d = d
        self.ns = ns

    def solve(self):
        v0 = 10 ** 100
        for (p, v) in self.ns:
            v0 = min(v0, 1.0 * self.d * v / (self.d - p))
        return v0

if __name__ == '__main__':
    T = int(raw_input())
    for case_ in xrange(T):
        (d, n) = map(int, raw_input().split())
        ns = []
        for i in xrange(n):
            (a, b) = map(int, raw_input().split())
            ns.append((a, b))

        print 'Case #%d: %f' % (case_ + 1, Solution(d, ns).solve())
