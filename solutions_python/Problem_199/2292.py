def solve():
    S, K = input().split()
    S = list(S)
    K = int(K)
    c = 0
    while K <= len(S):
        while S and S[-1] == '+':
            S.pop()

        if S and K <= len(S):
            c += 1
            for i in range(K):
                j = -1 - i
                S[j] = '+' if S[j] == '-' else '-'

    return 'IMPOSSIBLE' if any(s == '-' for s in S) else c

T = int(input())
for t in range(1, T + 1):
    print ("Case #%d: %s" % (t, solve()))
