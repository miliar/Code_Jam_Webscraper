"""

"""

def get_diffs(mushrooms):
    return tuple(mushrooms[i-1] - mushrooms[i]
                 for i in xrange(1, len(mushrooms)))


def method1(diffs):
    return sum(d for d in diffs if d > 0)


def method2(diffs, mushrooms):
    try:
        min_rate = max(d for d in diffs if d > 0)
        return sum(min(min_rate, mushrooms[i])
                   for i in xrange(len(mushrooms) - 1))
    except ValueError:  # no min_rate
        return 0


def solve(diffs, mushrooms):
    y = method1(diffs)
    z = method2(diffs, mushrooms)
    return y, z


def std_in():
    while True:
        yield raw_input()


def main():
    STD_IN = std_in()

    T = int(next(STD_IN).strip())

    for t in xrange(T):
        N = int(next(STD_IN))
        mushrooms = map(int, next(STD_IN).strip().split())
        diffs = get_diffs(mushrooms)
        y, z = solve(diffs, mushrooms)
        print 'Case #{}: {} {}'.format(t+1, y, z)


if __name__ == '__main__':
    main()
