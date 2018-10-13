#!/usr/bin/python

def count_swaps(n, k, b, t, x, v):
    tt = [float(b-x[i])/v[i] for i in range(n)]
    good_ones = 0
    bad_ones = 0
    q = 0
    pos = n-1
    while pos >= 0 and good_ones < k:
        if tt[pos] <= t:
            good_ones += 1
            q += bad_ones
        else:
            bad_ones += 1
        pos -= 1
    return '%d' % q if good_ones >= k else 'IMPOSSIBLE'

if __name__ == '__main__':
    c = int(raw_input())
    for i in range(c):
        n, k, b, t = [int(s) for s in raw_input().split()]
        x = [int(s) for s in raw_input().split()]
        v = [int(s) for s in raw_input().split()]
        answer = count_swaps(n, k, b, t, x, v)
        print 'Case #%d: %s' % (i+1, answer)
