
import itertools, sys
from collections import defaultdict

class Continue(Exception):
    pass

class Scorer(object):
    def __init__(self):
        self.surp = defaultdict(set)
        self.not_surp = defaultdict(set)
        for a in range(11):
            for b in range(11):
                for c in range(11):
                    mxd = max(abs(a - b), abs(b - c), abs(a - c))
                    if mxd <= 2:
                        t = a + b + c
                        if mxd == 2:
                            self.surp[t].add(max(a, b, c))
                        else:
                            self.not_surp[t].add(max(a, b, c))

    def best(self, p, S, tpoints):
        perm = [(self.surp[tp], self.not_surp[tp]) for tp in tpoints]
        total = 0
        for surprising in itertools.combinations(range(len(tpoints)), S):
            choices = []
            try:
                for i in range(len(tpoints)):
                    if i in surprising:
                        choices.append(perm[i][0])
                    else:
                        choices.append(perm[i][1])
                    if len(choices[-1]) == 0:
                        raise Continue()
                total = max(self.nchoose(p, choices), total)
            except Continue:
                pass
        return total

    def nchoose(self, p, choices):
        total = 0
        for c in choices:
            if max(c) >= p:
                total += 1
        return total

if __name__ == '__main__':
    lines = sys.stdin.readlines()
#    lines = open('test.in', 'r').readlines()
    T = int(lines[0])
    t = 1
    score = Scorer()
    for line in lines[1:]:
        line = [int(i) for i in line.split()]
        N, S, p = line[0:3]
        tpoints = line[3:]
        assert len(tpoints) == N
        y = score.best(p, S, tpoints)
        print('Case #%d: %d' % (t, y))
        t += 1
