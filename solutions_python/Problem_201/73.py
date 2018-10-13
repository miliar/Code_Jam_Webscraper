# criteria for choosing next stall:
#
# L_S, R_S are number of empty stalls on left and right of stall
# choose stall with maximal min(L_S, R_S)
# failing that, choose stall with maximal max(L_S, R_S)
# failing that, choose leftmost stall
#
# so what effect does that actually have?
# stall will be chosen at maximum of largest interval; if there's an empty span
# of 2 k + 1 stalls, then L_S = R_S = k for center stall; if there's an empty
# span of 2 k stalls then L_S = k - 1 and R_S = k for left-of-center stall, L_S
# = k and R_S = k - 1 for right-of-center stall, so left-of-center stall gets
# chosen.
#
# so preference is for largest remaining interval, central choice. furthermore there will only be at most four size classes of intervals at any given point

# 1 x 100
# 1 x 50, 1 x 49
# 1 x 49, 1 x 25, 1 x 24
# 1 x 25, 3 x 24
# 3 x 24, 2 x 12
# 5 x 12, 3 x 11
# 3 x 11, 5 x 6, 5 x 5
# 5 x 6, 11 x 5
# 

from collections import Counter

def solve(n, k):
    s = [(n, 1)]
    def add_intervals(n, mult):
        if not s:
            s.append((n, mult))
            return
        last_n, last_mult = s[-1]
        assert last_n >= n
        if last_n == n:
            s[-1] = (n, last_mult + mult)
        else:
            s.append((n, mult))
    while s:
        n, mult = s.pop(0)
        ls = (n - 1) / 2
        rs = n / 2
        if k <= mult:
            return (rs, ls)
        k -= mult
        add_intervals(rs, mult)
        add_intervals(ls, mult)
    assert False, "reached end without hitting mult"

if __name__ == '__main__':
    import sys
    fp = open(sys.argv[1])
    def readline():
        return fp.readline().strip()
    num_cases = int(readline())
    for i in xrange(num_cases):
        n, k = [int(x) for x in readline().split()]
        ls, rs = solve(n, k)
        print "Case #%d: %d %d" % (i + 1, ls, rs)
