T = int(input())
for t in range(T):
    S, K = input().split()
    S = list(S)
    K = int(K)
    N = len(S)
    ans = True
    cnt = 0
    for i in range(N):
        if i + K <= N:
            if S[i] == "-":
                cnt += 1
                for j in range(i, i + K):
                    if S[j] == "-":
                        S[j] = "+"
                    else:
                        S[j] = "-"
        else:
            if S[i] == "-":
                ans = False
                break
    if ans:
        print("Case #{}: {}".format(t + 1, cnt))
    else:
        print("Case #{}: IMPOSSIBLE".format(t + 1))
