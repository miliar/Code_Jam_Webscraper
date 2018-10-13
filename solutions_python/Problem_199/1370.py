'''input
3
---+-++- 3
+++++ 4
-+-+- 4
'''
T = int(input())
for t in range(T):
    S, K = input().split()
    S, K = list(S), int(K)
    N = len(S)
    res = 0
    for i in range(N - K + 1):
        if S[i] == "-":
            res += 1
            for j in range(K):
                S[i + j] = "-" if S[i + j] == "+" else "+"

    print("Case #{}: {}".format(t+1, "IMPOSSIBLE" if '-' in S else res))