#!/usr/bin/python3

def solve(t):
    s, sk = input().split()
    k = int(sk)
    n = len(s)
    flip = [0 for i in range(n + 1)]
    cflip = 0
    ans = 0
    for i in range(n - k + 1):
        cflip ^= flip[i]
        u = 0 if s[i] == '+' else 1
        u ^= cflip
        if u:
            ans += 1
            flip[i] ^= 1
            flip[i + k] ^= 1
            cflip ^= 1
    ok = True
    for i in range(n - k + 1, n):
        cflip ^= flip[i]
        u = 0 if s[i] == '+' else 1
        u ^= cflip
        if u:
            ok = False
    if ok:
        print("Case #{}: {}".format(t, ans))
    else:
        print("Case #{}: IMPOSSIBLE".format(t))
        


n_o_t = int(input())
for i in range(n_o_t):
    solve(i + 1)
