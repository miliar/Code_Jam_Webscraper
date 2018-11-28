import sys

# Alphabetically earliest: PRS
# Pair -> winner
# PR -> P
# PS -> S
# RS -> R


#  S
#  PS
# PR PS

#  R
#  SR
# PS RS

#  P
#  PR
# PR RS

from collections import defaultdict

Default = defaultdict(dict)
Default[1]['S'] = 'PS'
Default[1]['R'] = 'RS'
Default[1]['P'] = 'PR'

def to_get(winner, depth):
    if depth == 1:
        return Default[1][winner]
    ret = []
    left, right = to_get(winner, 1)

    lh = to_get(left, depth-1)
    rh = to_get(right, depth-1)

    if lh < rh:
        ans = lh + rh
    else:
        ans = rh + lh

    Default[depth][winner] = ans

    return ans

def solve(N, R, P, S):
    if any( (x > 2**(N-1)) for x in [R,P,S]):
        return 'IMPOSSIBLE'

    r1 = to_get('R', N)
    r2 = to_get('P', N)
    r3 = to_get('S', N)

    def can_do(r):
        return R == r.count('R') and P == r.count('P') and S == r.count('S')

    ret = []
    if can_do(r1):
        ret.append(r1)
    if can_do(r2):
        ret.append(r2)
    if can_do(r3):
        ret.append(r3)

    if not ret:
        return 'IMPOSSIBLE'

    return min(ret)

def main():
    T = int(sys.stdin.readline().strip())

    for i in xrange(T):
        N, R, P, S = map(int, sys.stdin.readline().strip().split())
        ans = solve(N, R, P, S)
        print 'Case #%s: %s' % (i+1, ans)

if __name__ == '__main__':
    main()
