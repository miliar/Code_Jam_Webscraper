import sys

def worst_winner(N, P):
    p = 0

    while 2**(p + 1) - 1 < P:
        p += 1

    wins = N - p
    return 2**N - 2**wins

def best_loser(N, P):
    if P == 2**N:
        return 2**N
    else:
        return 2**N - 1 - worst_winner(N, 2**N - P)

def solve_case(test_case):
    N, P = map(int, raw_input().split())
    print "Case #{0}: {1} {2}".format(test_case, best_loser(N, P) - 1, worst_winner(N, P))

for test_case in xrange(1, int(raw_input()) + 1):
    solve_case(test_case)
    sys.stdout.flush()