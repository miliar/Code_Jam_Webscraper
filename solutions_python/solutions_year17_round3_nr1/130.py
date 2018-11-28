from math import pi
T = int(input())
for case in range(1, T+1):
    best_result = 0
    n, k = map(int, input().split())
    panc = [list(map(int, input().split())) for _ in range(n)]
    panc.sort()
    for start in range(0, n-k+1):
        if start == 0:
            p_cop = panc[:]
        else:
            p_cop = panc[:-start]
        # print(k, len(p_cop))
        fir = p_cop.pop()
        # print(p_cop)
        result = fir[0] * pi * (fir[0] + 2*fir[1])
        p_cop.sort(key=lambda x: x[0]*x[1])
        # print(p_cop)
        for i in range(k-1):
            fir = p_cop.pop()
            result += fir[0] * pi * 2 * fir[1]
        best_result = max(result, best_result)
        # print(panc)
    print(f"Case #{case}: {best_result:.10f}")
