
import sys
in_ = sys.stdin

T = int(in_.readline())
for t in xrange(T):
    N = int(in_.readline())
    A = map(float, in_.readline().split(' '))
    B = map(float, in_.readline().split(' '))

    a, b = sorted(A), sorted(B)
    score_war = 0
    while a:
        v1 = a.pop(-1)
        xx = [i for i, x in enumerate(b) if x > v1]
        v2 = b.pop(xx[0] if xx else 0)
        score_war += 1 if v1 > v2 else 0

    a, b = sorted(A), sorted(B)
    score_dwar = 0
    while a:
        xx = [i for i, x in enumerate(a) if x > b[0]]
        v1_take = a.pop(xx[0] if xx else 0)
        v1_tell = 1.0 if xx else b[-1] - 1e-6
        xx = [i for i, x in enumerate(b) if x > v1_tell]
        v2 = b.pop(xx[0] if xx else 0)
        score_dwar += 1 if v1_take > v2 else 0

    print 'Case #%d: %d %d' % (t + 1, score_dwar, score_war)
