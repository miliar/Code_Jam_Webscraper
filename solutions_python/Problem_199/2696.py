def s_to_i(s):
    if s == '-':
        return -1
    return 1

def solve(S, K):
    n_flips = 0
    for i in range(len(S) - K + 1):
        if S[i] == -1:
            n_flips += 1
            for j in range(K):
                S[i + j] *= -1

    if all(s == 1 for s in S):
        return n_flips
    return -1


T = int(input())
for t in range(T):
    S, K = input().split()
    S = list(map(s_to_i, S))
    K = int(K)
    answer = solve(S, K)
    if answer == -1:
        answer = 'IMPOSSIBLE'
    print('Case #{}: {}'.format(t + 1, answer))
