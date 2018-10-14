#! /usr/bin/env python3


def nrevs(ans, k, i):
    l, r = -1, len(ans)
    while r - l > 1:
        m = (r + l) // 2
        if ans[m] + k - 1 >= i:
            r = m
        else:
            l = m
    return len(ans) - r


for test in range(1, int(input()) + 1):
    s, k = input().split()
    k = int(k)
    s = [c == '+' for c in s]
    ans = []
    for i, c in enumerate(s):
        if not (c ^ (nrevs(ans, k, i) % 2 == 1)):
            if len(s) - i >= k:
                ans.append(i)
            else:
                print('Case #{}: {}'.format(test, 'IMPOSSIBLE'))
                break
    else:
        print('Case #{}: {}'.format(test, len(ans)))
