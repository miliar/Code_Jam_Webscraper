import argparse, math

ap = argparse.ArgumentParser()
ap.add_argument('input', type=argparse.FileType('r'))
args = ap.parse_args()
toks = args.input.read().split()
toks.reverse()

T = int(toks.pop())
for t in xrange(T):
    N = int(toks.pop())
    P = int(toks.pop())
    G = [int(toks.pop()) for i in xrange(N)]

    M = [g % P for g in G]

    if P == 2:
        r = M.count(0)
        r += (N - r + 1) // 2
    elif P == 3:
        r = M.count(0)

        g1 = M.count(1)
        g2 = M.count(2)

        m = min(g1, g2)
        r += m
        g1 -= m
        g2 -= m

        r += (g1 + g2 + 2) // 3

    print 'Case #{}: {}'.format(t + 1, r)
