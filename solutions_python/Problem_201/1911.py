#!/usr/bin/python

def noneif(x):
    return -1 if x is None else x

def update(stall, l, r, n):
    for i in xrange(1, n+1):
        if stall[i] == 'O':
            l[i] = None
        else:
            l[i] = noneif(l[i-1]) + 1
    for i in xrange(n, 0, -1):
        if stall[i] == 'O':
            r[i] = None
        else:
            r[i] = noneif(r[i+1]) + 1

def get_best_stall(stall, l, r, n):
    min_lr = map(min, zip(l, r))
    max_lr = map(max, zip(l, r))

    max_min = max(min_lr)
    stall_id_with_max_min = [i for i, x in enumerate(min_lr) if x == max_min]

    max_max = max(map(lambda x: max_lr[x], stall_id_with_max_min))
    stall_id_with_max_max = filter(lambda x: max_lr[x] == max_max, stall_id_with_max_min)

    leftmost = stall_id_with_max_max[0]
    return leftmost

def solve(case_no):
    n, k = map(int, raw_input().split())
    stall = list('O' + '.'*n + 'O')
    l, r = [None] * (n+2), [None] * (n+2)

    for i in xrange(k):
        update(stall, l, r, n)
        idx = get_best_stall(stall, l, r, n)
        stall[idx] = 'O'

    y, z = max(l[idx], r[idx]), min(l[idx], r[idx])
    print 'Case #%d: %d %d' % (case_no, y, z)

t = int(raw_input())
for case_no in xrange(1, t+1):
    solve(case_no)
