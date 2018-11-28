import sys


def optimal_score(a,b):
    i = j = 0
    score_a = score_b = 0
    while score_a + score_b < len(a):
        if a[i] > b[j]:
            score_a += 1
            i += 1
            j += 1
        else:
            score_b += 1
            i += 1
    return score_a


def score_without_cheating(a,b):
    a.reverse()
    b.reverse()
    i = j = 0
    score_a = score_b = 0

    while score_a + score_b < len(a):
        if a[i] > b[j]:
            score_a += 1
            i += 1
        else:
            score_b += 1
            i += 1
            j += 1

    return score_a


def solve(t):
    N = int(sys.stdin.readline())
    a = [float(x) for x in sys.stdin.readline().split()]
    b = [float(x) for x in sys.stdin.readline().split()]
    assert len(a) == len(b)
    a.sort()
    b.sort()
    op_score = optimal_score(a,b)
    no_cheat_score = score_without_cheating(a,b)
    sys.stdout.write('Case #%i: %i %i\n' % (t, op_score, no_cheat_score))


T = int(sys.stdin.readline())
for t in range(1, T+1):
    solve(t)
