from math import log

def function(n, k):
    q, d = divmod(log(k) / log(2), 1)
    # see 2017.C.xlsx for proof
    if 1. * (n - k) / (2. ** q) < 1.:
        return 0, 0
    elif 1. * (n - k) / (2. ** q) < 2.:
        return 1, 0
    elif 1. * (n - k) / (2. ** q) < 3.:
        return 1, 1
    elif 1. * (n - k) / (2. ** q) < 4.:
        return 2, 1
    elif 1. * (n - k) / (2. ** q) < 5.:
        return 2, 2
    elif 1. * (n - k) / (2. ** q) < 6.:
        return 3, 2
    elif 1. * (n - k) / (2. ** q) < 7.:
        return 3, 3
    # stalls[x] = 0 if occupied, otherwise the length of unoccupied
    # contiguous stalls around x
    stalls = [0] + [n] * n + [0]
    ls = -1
    rs = -1
    for people in xrange(k):
        # largest number in stalls
        rank = max(stalls)
        # leftmost bloc [left, right] within stalls whose stall
        # equal to largest number
        left = -1
        right = -1
        for stall in xrange(1, n + 1):
            if stalls[stall] == rank:
                if left == -1:
                    left = stall
                right = stall
            elif left > 0:
                break
        # stall chosen is the middle of [left, right]
        # integer division rounds down which gives the correct stall
        middle = (left + right) / 2
        # adjust stalls in the [left, right] section
        ls = middle - left
        rs = right - middle
        stalls[middle] = 0
        for stall in xrange(left, middle):
            stalls[stall] = ls
        for stall in xrange(middle + 1, right + 1):
            stalls[stall] = rs
    return max(ls, rs), min(ls, rs)

T = int(raw_input().strip())  # read a line with a single integer

for i in xrange(1, T + 1):
    n, k = map(int, raw_input().strip().split(' '))  # read input
    print "Case #{}: {} {}".format(i, *function(n, k))
