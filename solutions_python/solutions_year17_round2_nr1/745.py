def solve():
    D, N = (int(x) for x in input().split())
    K, S = [], []
    for i in range(N):
        k, s = (int(x) for x in input().split())
        K.append(k)
        S.append(s)

    maxT = 0.0
    for i in range(N):
        t = float(D - K[i]) / S[i] # t = S/V
        maxT = max(maxT, t)

    return float(D) / maxT # V = S/t

T = int(input())
for t in range(1, T + 1):
    print ("Case #%d: %.6f" % (t, solve()))
