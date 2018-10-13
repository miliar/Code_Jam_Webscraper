import sys


def solve_problem(a, b, k):
    winning = set(range(k))
    res = 0
    for i in xrange(a):
        for j in xrange(b):
            if i & j in winning:
                res += 1

    return res


if __name__ == "__main__":
    num_of_cases = int(sys.stdin.readline().strip())

    for i in xrange(1, num_of_cases + 1):
        a, b, k = map(int, sys.stdin.readline().strip().split())
        print "Case #{0}: {1}".format(i, solve_problem(a, b, k))
