from math import sqrt
T = input()
for case in range(1, T + 1):
    L, P, C = map(int, raw_input().split())
    D = float(P) / L
    ans = 0
    while D > C:
        ans += 1
        D = sqrt(D)
    print 'Case #%s: %s' % (case, ans)
