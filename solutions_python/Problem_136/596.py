import sys

def solve_case(test_case):
    C, F, X = map(float, raw_input().split())
    rate = 2.0
    base = 0.0
    best = X / rate

    while True:
        base += C / rate
        rate += F
        current = base + X / rate

        if current < best:
            best = current
        else:
            break

    print "Case #%d: %.9lf" % (test_case, best)

for test_case in xrange(1, int(raw_input()) + 1):
    solve_case(test_case)
    sys.stdout.flush()
