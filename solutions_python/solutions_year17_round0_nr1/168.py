def solve(i):
    S, K = input().split(" ")
    K = int(K)
    S = list(S)
    n = len(S)
    result = 0
    for x in range(0,n - K + 1):
        if S[x] == '-':
            result += 1
            for y in range(x, x+K):
                S[y] = '+' if S[y] == '-' else '-'
    success = True
    for s in S:
        if s == '-':
            success = False
            break
    if success:
        print("Case #{}: {}".format(i, result))
    else:
        print("Case #{}: IMPOSSIBLE".format(i))













t = int(input())
for i in range(t):
    solve(i+1)