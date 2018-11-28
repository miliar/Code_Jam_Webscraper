import copy
import sys


def parse(f):
    D = int(f.readline())
    pancakes = map(int, f.readline().split())

    return D, pancakes


MEMO = {}


def solve(D, pancakes):
    pancakes.sort()
    highest_pile = pancakes[-1]

    if highest_pile < 4:
        MEMO[tuple(pancakes)] = highest_pile
        return highest_pile
    else:
        result = [0] * (highest_pile/2)

        for i in xrange(0, highest_pile/2):
            new = copy.copy(pancakes)

            new.remove(highest_pile)
            new.extend([i+1, highest_pile-i-1])
            
            t = tuple(new)
            if t in MEMO:
                result[i] = MEMO[t]
            else:
                result[i] = solve(D+1, new)
                MEMO[t] = result[i]

        return min(highest_pile, 1 + min(result))


def main():
    with open(sys.argv[1], "r") as input_file:
        T = int(input_file.readline())

        for i in xrange(T):
            D, pancakes = parse(input_file)
            result = solve(D, pancakes)

            print "Case #%d: %d" % (i+1, result)


if __name__ == "__main__":
    main()
