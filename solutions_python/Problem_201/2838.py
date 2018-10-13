def solve(N, K, case):
    S = [0 for x in range(N + 2)]
    S[0] = 1
    S[-1] = 1
    for i in range(0, K):
        L = 0
        R = 0
        pos = 1
        for x in range (1, N + 1):
            if not S[x]:
                tL = 1
                tR = 1
                while not S[x - tL]:
                    tL += 1
                while not S[x + tR]:
                    tR += 1
                tL -= 1
                tR -= 1
                pmin = min(L, R)
                cmin = min(tL, tR)
                if cmin >= pmin:
                    if cmin > pmin or (cmin == pmin and max(tL, tR) > max(L, R)):
                        L = tL
                        R = tR
                        pos = x
        S[pos] = 1
    print "Case #{}: {} {}".format(case, max(L,R) , min(L,R))

lines = input()
for i in range(1, lines + 1):
    n, m = [int(s) for s in raw_input().split(" ")]
    solve(n,m,i)
