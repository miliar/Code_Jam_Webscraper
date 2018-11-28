import sys


class Prob(object):
    def __init__(self, c, f, x):
        self.c = c
        self.f = f
        self.x = x

    def solve(self):
        baserate = 2
        rate = baserate
        t_expected = self.x/rate
        t_farm = self.c/rate + self.x/(baserate+self.f)
        ttotal = 0
        while (t_farm < t_expected):
            ttotal += self.c/rate
            rate += self.f
            t_expected = self.x/rate
            t_farm = self.c/rate + self.x/(rate+self.f)
        return t_expected + ttotal

output = "Case #%d: %s"

with open(sys.argv[1], 'r') as f:
    T = int(f.readline())
    for counter in xrange(T):
        line = f.readline()
        c, F, x = [float(i) for i in line.split()]
        p1 = Prob(c, F, x)
        print output % (counter+1, p1.solve())
