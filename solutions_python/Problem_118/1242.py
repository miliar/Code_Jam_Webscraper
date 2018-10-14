import sys
from math import sqrt, ceil, floor


class Prob3(object):
    def __init__(self, limita, limitb):
        # new limits
        self.limita, self.limitb = int(ceil(sqrt(limita))), int(floor(sqrt(limitb)))
        self.output = 0

    def solve(self):
        for x in range(self.limita, self.limitb + 1):
            if not self.is_palindrom(x):
                continue
            elif not self.is_palindrom(x*x):
                continue
            else:
                self.output += 1

        return self.output

    def is_palindrom(self, x):
        s = str(x)
        if s == s[::-1]:
            return True
        else:
            return False

output = "Case #%d: %d"

with open(sys.argv[1], 'r') as f:
    T = int(f.readline())
    for counter in xrange(T):
        line = f.readline()
        limita, limitb = [int(i) for i in line.strip().split(" ")]
        p = Prob3(limita, limitb)
        print output % (counter+1, p.solve())
