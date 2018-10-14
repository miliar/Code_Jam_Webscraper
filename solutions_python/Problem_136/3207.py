T = int(raw_input())

for case_num in range(1, T+1):
    C, F, X = map(float, raw_input().split())

    ans = 1e100

    t = 0.0
    prod = 2.0

    while t < ans:
        ans = min(ans, t + X / prod)
        t += C / prod
        prod += F

    print "Case #%d: %f" % (case_num, ans)
