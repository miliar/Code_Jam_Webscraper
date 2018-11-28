import sys


class Prob1(object):
    def __init__(self, smax, s):
        self.smax = smax
        self.s = s

    def solve(self):
        added = 0
        satisfied = self.s[0]
        for i, j in enumerate(self.s):
            if i == 0:
                continue
            if i > satisfied:
                added += i - satisfied
                satisfied = i
            satisfied += j

        return added


output = "Case #%d: %s"

with open(sys.argv[1], 'r') as f:
    T = int(f.readline())
    for counter in xrange(T):
        data = f.readline().split()
        smax = int(data[0])
        s = [int(j) for j in data[1]]
        p1 = Prob1(smax, s)
        print output % (counter+1, p1.solve())
