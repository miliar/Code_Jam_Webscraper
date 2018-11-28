import sys

def gcd(a, b):
    return b if a == 0 else gcd(b % a, a)

def is_power_of_two(n):
    return n == (n & -n)

def solve_case(test_case):
    P, Q = map(int, raw_input().split('/'))
    g = gcd(P, Q)
    P /= g
    Q /= g

    if not is_power_of_two(Q):
        print "Case #%d: impossible" % test_case
        return

    generations = 0

    while P < Q:
        P *= 2
        generations += 1

    print "Case #%d: %d" % (test_case, generations)

for test_case in xrange(1, int(raw_input()) + 1):
    solve_case(test_case)
    sys.stdout.flush()
