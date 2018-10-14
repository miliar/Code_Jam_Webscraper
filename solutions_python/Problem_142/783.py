import sys
import itertools


class Prob1(object):
    def __init__(self, n, strings):
        self.n = n
        self.strings = strings

    def solve(self):
        actions = 0

        if self.is_possible():
            if self.n == 2:
                # naive implementation
                data1 = []
                data2 = []

                for ch, it in itertools.groupby(self.strings[0]):
                    data1.append(len(list(it)))

                for ch, it in itertools.groupby(self.strings[1]):
                    data2.append(len(list(it)))

                a = [abs(x - y) for x, y in zip(data1, data2)]
                actions = sum(a)
                return actions
        else:
            return "Fegla Won"

    def is_possible(self):
        strings2 = []
        for i in strings:
            strings2.append(
                ''.join(ch for ch, _ in itertools.groupby(i)))

        if len(set(strings2)) == 1:
            return True
        else:
            return False

output = "Case #%d: %s"

with open(sys.argv[1], 'r') as f:
    T = int(f.readline())
    for counter in xrange(T):
        N = int(f.readline())
        strings = []
        for i in xrange(0, N):
            strings.append(f.readline())
        p1 = Prob1(N, strings)
        print output % (counter+1, p1.solve())
