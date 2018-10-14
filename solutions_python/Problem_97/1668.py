import itertools, sys

class Case(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def run(self):
        results = set()
        for i in range(self.start, self.end):
            for a, b in self.get_combinations(str(i)):
                if a < b and a in self.get_series(str(b)):
                    results.add((a,b,))

        #print 'result: %s' % str(results)
        return len(results)

    def get_series(self, value):
        series = []
        length = len(value)
        for i in range(0, length):
            series.append(int(value[i:] + value[0:i]))

        #print 'series(%s): %s' % (value, str(series),)
        return series

    def get_combinations(self, value):
        numbers = []
        for n in self.get_series(value):
            if self.start <= n and self.end >= n:
                numbers.append(n)

        #print 'numbers(%s): %s' % (value, str(numbers),)
        #print 'combinations:', str([c for c in itertools.combinations(sorted(numbers), 2)])

        #return itertools.combinations(sorted(numbers), 2)
        return set(itertools.permutations(numbers, 2))

def main(args=sys.argv[1:]):
    cases = []

    with open(args[0]) as f:
        n = int(f.readline())
        for l in f:
            cases.append(Case(*[int(number) for number in l.split()]))

    for i, c in enumerate(cases):
        print 'Case #%d: %d' % (i+1, c.run(),)

    return 0

if __name__ == '__main__':
    sys.exit(main())
