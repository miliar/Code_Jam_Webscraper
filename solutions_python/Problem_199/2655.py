import sys


class Prob(object):
    def __init__(self, pancakes, k):
        self.pancakes = list(pancakes)
        self.k = k

    def flip(self, i):
        for j in xrange(self.k):
            if self.pancakes[i+j] == '-':
                self.pancakes[i+j] = '+'
            else:
                self.pancakes[i+j] = '-'

    def solve(self):
        flips = 0

        #  -----
        #     +++

        for i in xrange(len(self.pancakes)):
            if self.pancakes[i] == '-' and i <= len(self.pancakes) - k:
                self.flip(i)
                flips += 1

        if '-' in self.pancakes:
            flips = 'IMPOSSIBLE'

        return flips

cases = int(sys.stdin.readline())

for case in xrange(cases):
    line = sys.stdin.readline().split()

    pancakes = line[0]
    k = int(line[1])

    prob = Prob(pancakes, k)

    print 'Case #{}: {}'.format(case+1, prob.solve())
