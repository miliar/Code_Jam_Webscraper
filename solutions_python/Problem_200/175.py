#!/usr/bin/env python3

def solve(N):
    N = [int(c) for c in N]  # list of digits

    def recur(s, pos, val, dropped):
        if pos >= len(s):
            return []

        cur = 9 if dropped else s[pos]
        next_dropped = dropped

        while cur >= val:
            ret = recur(s, pos+1, cur, next_dropped)
            if ret is not None:
                return [cur] + ret
            cur -= 1
            next_dropped = True

        return None

    ret = recur(N, 0, 0, False)
    ret_str = ''.join(map(str, ret)).lstrip('0')
    return ret_str


T = int(input())
for t in range(T):
    a = input()
    res = solve(a)
    print('Case #{}: {}'.format(t+1, res))

