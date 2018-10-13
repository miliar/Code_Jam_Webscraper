import sys

class CandyPile(object):
    def __init__(self):
        self.sean = 0
        self.patrick = 0
    def add(self, candy):
        self.sean += candy
        self.patrick ^= candy
    def is_good(self):
        return self.sean >= self.patrick
    def copy(self):
        c = CandyPile()
        c.sean = self.sean
        c.patrick = self.patrick
        return c

class CandySplit(object):
    def __init__(self, candy):
        self.candy = candy
        
    def solve(self):
        trials = [[CandyPile(), CandyPile()]]
        for c in self.candy:
            new_trials = []
            for (sean, patrick) in trials:
                adds = sean.copy()
                adds.add(c)
                addp = patrick.copy()
                addp.add(c)
                new_trials.append((adds, patrick))
                new_trials.append((sean, addp))
            trials = new_trials
        values = [s.sean for (s, p) in trials if s.patrick == p.patrick and s.sean != 0 and p.sean != 0]
        if len(values) == 0:
            return 0
        values.sort()
        return values[-1]


def read_test_case(instream):
    N = int(instream.readline())
    candy = map(int, instream.readline().split())
    assert(N == len(candy))
    return candy

if __name__ == '__main__':
    instream = sys.stdin
    #instream = open('test.small.in')
    outstream = sys.stdout
    test_cases = int(instream.readline())
    for i in range(test_cases):
        case = read_test_case(instream)
        cs = CandySplit(case)
        value = cs.solve()
        if value == 0:
            result = 'NO'
        else:
            result = '%d' % value
        outstream.write("Case #%d: %s\n" % (i + 1, result))
