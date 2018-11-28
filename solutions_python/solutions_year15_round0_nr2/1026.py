from __future__ import division
import math

inf = float("inf")


def solve(pancakes):
    dp = []

    for plate in pancakes:
        d = {}
        for i in xrange(1, plate + 1):
            div = int(math.ceil(plate / i))

            if (div not in d) or (d[div] > i - 1):
                d[div] = i - 1

        print plate
        print d

        dp.append(d)


    return try_recursively(dp, 0, 0, 0)



def try_recursively(dp, pos, _max, splits):
    if pos == len(dp):
        return _max + splits

    _min = inf

    for key, value in dp[pos].iteritems():
        pot_min = try_recursively(dp, pos + 1, max(_max, key), splits + value)

        _min = min(_min, pot_min)

    return _min


def main():
    f1 = open('pancakes.out', 'w')

    with open('pancakes.in', 'r') as f:
        cases = int(f.readline())

        for t in xrange(1, cases + 1):
            f.readline()

            case = f.readline()

            case = case.strip('\n')

            as_str = case.split(' ')

            pancakes = map(int, list(as_str))

            print >>f1, "Case #" + str(t) + ": " + str(solve(pancakes))

if __name__ == '__main__':
    main()
