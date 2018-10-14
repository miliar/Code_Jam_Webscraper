def solve(D, N, K, S):
    NeedTime = [float(D - K[n]) / S[n] for n in range(N)]
    longestTime = sorted(NeedTime)[-1]
    return float(D) / longestTime

T = input()
for t in range(1, T + 1):
    D, N = map(int, raw_input().split())
    K, S = [], []
    for n in range(N):
        k, s = map(int, raw_input().split())
        K.append(k)
        S.append(s)
    print 'Case #%d: %.6f'%(t, solve(D, N, K, S))
