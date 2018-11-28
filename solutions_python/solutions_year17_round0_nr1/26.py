def solve():
    S, K = input().split()
    S = [c for c in S]
    K = int(K)
    N = len(S)
    ans = 0
    while True:
        pos = -1
        for i in range(N):
            if S[i] == '-':
                pos = i
                break
        if pos == -1:
            print(ans)
            return
        if pos > N-K:
            print('IMPOSSIBLE')
            return
        ans += 1
        for i in range(pos, pos+K):
            if S[i] == '+':
                S[i] = '-'
            else:
                S[i] = '+'


T = int(input())
for num in range(1, T+1):
    print('Case #' + str(num) + ': ', end='')
    solve()
