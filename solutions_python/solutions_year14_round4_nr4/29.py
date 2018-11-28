def solve(num):
    M, N = map(int, input().split())
    W = []
    for i in range(M):
        W.append(input())
    ans = 0
    count = 0
    for perm in range(N ** M):
        A = []
        for i in range(M):
            A.append(perm % N)
            perm //= N
        if len(set(A)) < N:
            continue
        currans = 0
        for i in range(N):
            S = {""}
            for j in range(M):
                if A[j] == i:
                    for k in range(1, len(W[j]) + 1):
                        S.add(W[j][:k])
            currans += len(S)
        if currans > ans:
            ans = currans
            count = 1
        elif currans == ans:
            count += 1
    print("Case #" + str(num) + ":", ans, count % (10 ** 9 + 7))

T = int(input())
for i in range(T):
    solve(i + 1)

