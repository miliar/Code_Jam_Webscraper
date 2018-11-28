#!/usr/bin/env python

fin = open("3.in", "r")
fout = open("3.out", "w")

infty = 1000000000

def solve(Hd, Ad, Hk, Ak, B, D, b, d):
    # debuff d times, then buff b times, then attack until dead
    ans = 0
    Hc = Hd
    while d > 0:
        ans += 1
        if ans > 200:
            return infty
        if Hc <= Ak - D:
            Hc = Hd
            Hc -= Ak
        else:
            Ak -= D
            d -= 1
            Hc -= Ak
    while b > 0:
        ans += 1
        if ans > 200:
            return infty
        if Hc <= Ak:
            Hc = Hd
            Hc -= Ak
        else:
            Ad += B
            b -= 1
            Hc -= Ak
    while Hk > 0:
        ans += 1
        if ans > 200:
            return infty
        if Hk <= Ad:
            return ans
        if Hc <= Ak:
            Hc = Hd
            Hc -= Ak
        else:
            Hk -= Ad
            Hc -= Ak

    return ans


T = int(fin.readline())
for t in range(T):
    print t+1
    Hd, Ad, Hk, Ak, B, D = map(int, fin.readline().split())
    ans = infty
    ans_b = 0
    ans_d = 0
    for b in range(Hk + 1):
        for d in range(Ak + 1):
            if B == 0 and b > 0:
                continue
            if D == 0 and d > 0:
                continue
            cur_ans = solve(Hd, Ad, Hk, Ak, B, D, b, d)
            if ans > cur_ans:
                ans = cur_ans
                ans_b = b
                ans_d = d

    print ans_b, ans_d

    if ans >= infty:
        ans = "IMPOSSIBLE"
    fout.write("Case #" + str(t+1) + ": " + str(ans) + "\n")
