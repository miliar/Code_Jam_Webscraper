#!/usr/bin/python3
t = int(input())

for it in range(1, t+1) :
    N, R, O, Y, G, B, V = [int(i) for i in input().split()]
    m = max(V+R+O, O+Y+G, G+B+V)
    if m * 2 > N:
        ans = "IMPOSSIBLE"
    elif V+O+G > 0:
        assert 0
        ans = "TOO HARD"
    else:
        li = -1
        ans = ""
        c = [R, Y, B]
        i0 = 0 if c[0] == m else 1 if c[1] == m else 2
        while len(ans) < N:
            m = max(c)
            i = i0 if c[i0] == m else 0 if c[0] == m else 1 if c[1] == m else 2
            if i == li:
                ii, iii = (i+1)%3, (i+2)%3
                i = ii if c[ii] >= c[iii] or c[ii] == c[iii] and ii == i0 else iii
            ans += "RYB"[i]
            li = i
            c[i] -= 1
        assert ans[0] != ans[-1]
    print("Case #%d:"%it, ans)
