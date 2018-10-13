def flip(S, start, end):
    for i in range(start, end):
        S[i] = '+' if S[i] == '-' else '-'

T = int(input())

for i in range(1, T+1):
    S, K = input().split()
    S = [s for s in S]
    K = int(K)
    ans = 0

    for j in range(len(S) - K + 1):
        if S[j] == '+':
            continue

        flip(S, j, j+K)
        ans += 1

    for j in range(len(S) - K + 1, len(S)):
        if S[j] == '-':
            ans = 'IMPOSSIBLE'
            break

    print(f'Case #{i}: {ans}')