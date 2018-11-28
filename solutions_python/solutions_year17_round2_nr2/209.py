import sys
from datetime import datetime


def debug(x):
    sys.stderr.write('{} DEBUG: {}\n'.format(datetime.now().time(), x))

IMPOSSIBLE = "IMPOSSIBLE"

def solve(N, R, O, Y, G, B, V):
    ans = []
    l = list(sorted([(R, 'R'), (B, 'B'), (Y, 'Y')]))
    for i in xrange(3):
        l[i] = (l[i][0], i, l[i][1])
    inl = list(l)
    prv = 'x'
    while N>0:
        l = list(sorted(l))
        #debug(l)
        #debug(ans)
        rem, ordd, c = l[-1]
        ind = -1
        if prv == c:
            rem, ordd, c = l[-2]
            ind = -2
        if not rem:
            #debug('here')
            return IMPOSSIBLE
        rem -= 1
        prv = c
        ans.append(c)
        l[ind] = (rem, ordd, c)
        N-=1

    if ans[0] == ans[-1]:
        return IMPOSSIBLE
    return ''.join(ans)


def main():
    T = int(raw_input())
    for tc in xrange(1, T+1):
        N, R, O, Y, G, B, V = map(int, raw_input().split())
        debug("Running test #{}...\n".format(tc))
        print "Case #{}: {}".format(tc, solve(N, R, O, Y, G, B, V))


if __name__ == "__main__":
    main()
