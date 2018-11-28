import sys

def deceitful(N, naomi, ken):
    total = 0
    n = 0

    for i in xrange(N):
        while n < N and naomi[n] < ken[i]:
            n += 1

        if n >= N:
            break

        n += 1
        total += 1

    return total

def war(N, naomi, ken):
    total = 0
    k = 0

    for i in xrange(N):
        while k < N and ken[k] < naomi[i]:
            k += 1

        if k >= N:
            break

        k += 1
        total += 1

    return N - total

def solve_case(test_case):
    N = int(raw_input())
    naomi = sorted(map(float, raw_input().split()))
    ken = sorted(map(float, raw_input().split()))
    print "Case #%d: %d %d" % (test_case, deceitful(N, naomi, ken), war(N, naomi, ken))

for test_case in xrange(1, int(raw_input()) + 1):
    solve_case(test_case)
    sys.stdout.flush()
