def solve(S: str, K: int):
    S = list(S)
    flips = 0
    while '-' in S:
        first_minus = S.index('-')
        if first_minus > len(S) - K:
            return 'IMPOSSIBLE'
        S[first_minus:first_minus+K] = ['-' if x == '+' else '+' for x in S[first_minus:first_minus+K]]
        flips += 1
    return flips


n_problems = int(input())
for i in range(n_problems):
    S, K = input().split(' ')
    K = int(K)
    print('Case #{}: {}'.format(i + 1, solve(S, K)))
