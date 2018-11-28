C = int(raw_input())
for c in range(C):
    N, K, B, T = [int(s) for s in raw_input().split()]
    X = [int(s) for s in raw_input().split()]
    V = [int(s) for s in raw_input().split()]
    able = [True if X[i] + V[i] * T >= B else False for i in range(N)]
    if able.count(True) < K:
        result = 'IMPOSSIBLE'
    else:
        result = 0
        swaps = 0
        j = 0
        for i in range(N - 1, -1, -1):
            if able[i]:
                j += 1
                result += swaps
                if j is K:
                    break
            else:
                swaps += 1
    print 'Case #{0}: {1}'.format(c + 1, result)
