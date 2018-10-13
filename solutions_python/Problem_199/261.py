def flip(x):
    return '+' if x == '-' else '-'

def solve(S, K):
    c = 0
    for i in range(len(S)-K+1):
        if S[i] == '-':
            c += 1
            for j in range(i,i+K):
                S[j] = flip(S[j])
    if all(x=='+' for x in S):
        return c
    else:
        return 'IMPOSSIBLE'

for case in range(1, int(input())+1):
    S, K = input().split()
    answer = solve(list(S), int(K))
    print('Case #{}: {}'.format(case, answer))
