import sys


class Prob(object):
    def __init__(self, n):
        self.n = [int(i) for i in n]

    def transform(self, j):
        # from j to the end -> 999
        # from j to the beginning go down until possible

        left = int(''.join(str(k) for k in self.n[0:j+1])) - self.n[j] - 1
        left = [k for k in str(left)]
        substract = 0
        while '0' in left:
            for i, value in enumerate(left):
                if value == '0':
                    substract = 10 ** (len(left) - i - 1)
            left = int(''.join(k for k in left))
            left -= substract
            left = [k for k in str(left)]
        right = [9 for _ in xrange(len(self.n)-j - 1)]
        highest = left + right
        return highest

    def solve(self):
        highest = list(self.n)

        previous = self.n[0]

        for j in xrange(len(self.n)):
            if previous > self.n[j]:
                while j > 1:
                    if self.n[j-1] == self.n[j-2]:
                        j -= 1
                    else:
                        break
                highest = self.transform(j)
                break

            previous = self.n[j]

        return ''.join((str(i) for i in highest))

cases = int(sys.stdin.readline())

for case in xrange(cases):
    line = sys.stdin.readline().strip()

    n = line

    prob = Prob(n)

    print 'Case #{}: {}'.format(case+1, prob.solve())
