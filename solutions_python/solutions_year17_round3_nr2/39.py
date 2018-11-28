#!/usr/bin/env python3

import math
import sys

def dur(r):
    return r[1] - r[0]

def solve(C, J):
    remain_c = 720 - sum(map(dur, J))
    remain_j = 720 - sum(map(dur, C))

    A = [(r[0], r[1], 'J') for r in C] + [(r[0], r[1], 'C') for r in J]
    A.sort()

    count = 0
    gap_cc = []
    gap_jj = []
    gap_cj = []

    for i in range(len(A)):
        pre, post = A[i-1], A[i]
        dist = (post[0] - pre[1]) % 1440

        if pre[2] != post[2]:
            count += 1
        if dist == 0:
            continue

        if pre[2] == post[2] == 'C':
            gap_cc.append((dist, pre, post))
        elif pre[2] == post[2] == 'J':
            gap_jj.append((dist, pre, post))
        else:
            gap_cj.append((dist, pre, post))


    # for gap_cc and gap_jj
    # fill smallest gaps first

    gap_cc.sort(reverse=True)
    while remain_c > 0 and gap_cc and gap_cc[-1][0] <= remain_c:
        gap = gap_cc.pop()
        remain_c -= gap[0]
        #print('filling gap (cc):', gap, file=sys.stderr)

    gap_jj.sort(reverse=True)
    while remain_j > 0 and gap_jj and gap_jj[-1][0] <= remain_j:
        gap = gap_jj.pop()
        remain_j -= gap[0]
        #print('filling gap (jj):', gap, file=sys.stderr)


    # one of them must be empty now, right?
    assert (not gap_cc) or (not gap_jj)

    '''
    print('final remain_c:', remain_c, file=sys.stderr)
    print('final remain_j:', remain_j, file=sys.stderr)

    print('remaining gap_cc:', gap_cc, file=sys.stderr)
    print('remaining gap_jj:', gap_jj, file=sys.stderr)
    print('remaining gap_cj:', gap_cj, file=sys.stderr)
    '''

    count += 2 * len(gap_cc)
    count += 2 * len(gap_jj)
    return count


T = int(input())
for t in range(T):
    ac, aj = map(int, input().split())
    c = [tuple(map(int, input().split())) for _ in range(ac)]
    j = [tuple(map(int, input().split())) for _ in range(aj)]
    #print(ac, aj, c, j)

    res = solve(c, j)
    print('Case #{}: {}'.format(t+1, res))

