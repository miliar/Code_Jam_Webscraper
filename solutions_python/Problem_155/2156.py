#!/usr/bin/env python3

def do_testcase():
    S_max, S = input().split()
    S_max = int(S_max)
    S = list(map(int, S))
    invite = total = 0
    for k in range(S_max + 1):
        if total >= S_max:
            break
        if total < k:
            n = k - total
            invite += n
            total += n
        total += S[k]
    else:
        n = S_max - total
        if n > 0:
            invite += S_max - total
    return max(0, invite)

T = int(input())
for t in range(1, T + 1):
    result = do_testcase()
    print('Case #{}: {}'.format(t, result))
