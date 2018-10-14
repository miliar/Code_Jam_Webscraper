T = int(input())
for i in range(1, T + 1):
    S, K = input().split()
    S = list(S)
    K = int(K)
    ans = 0
    for j in range(len(S) - K + 1):
        if S[j] == '-':
            for k in range(j, j + K):
                if S[k] == '-':
                    S[k] = '+'
                else:
                    S[k] = '-'
            ans += 1
    possibble = True
    for j in range(len(S) - K + 1, len(S)):
        if S[j] == '-':
            possibble = False
            break
    if not possibble:
        ans = 'IMPOSSIBLE'
    else:
        ans = str(ans)
    print("Case #%s: %s" % (str(i), ans))
