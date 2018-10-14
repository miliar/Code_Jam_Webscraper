def solve(S, K):
    S, K, flips = [1 if c == '+' else 0 for c in S], int(K), 0
    for i, c in enumerate(S):
        if i + K > len(S):
            break
        if not c:
            for j in range(i, i + K):
                S[j] = 1 - S[j]
            flips += 1
    return 'IMPOSSIBLE' if not all(S) else flips

if __name__ == '__main__':
    for i in range(int(input())):
        print('Case #{}: {}'.format(i + 1, solve(*input().split())))
