class Case(object):
    def __init__(self, data):
        self.data = data

    def solve(self):
        current = 0
        needed = 0
        added = 0
        for x in self.data:
            if x > 0:
                if needed > current:
                    added += needed - current
                    current += added
            current += x
            needed += 1
        return added


def parse_stdin():
    T = int(raw_input())
    cases = []
    for i in xrange(T):
        smax, data = raw_input().split(' ')
        data = [int(x) for x in data]
        cases.append(Case(data))
    return cases


def main():
    cases = parse_stdin()
    i = 1
    for c in cases:
        print 'Case #{:d}:'.format(i), c.solve()
        i += 1


if __name__ == '__main__':
    main()
