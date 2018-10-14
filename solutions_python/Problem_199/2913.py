
def oversized_pancake_flipper(S, k):
    moves = 0
    while False in S:
        i = S.index(False)
        if i > len(S) - k:
            return -1
        S[i:i+k] = list(map(lambda s: not s, S[i:i+k]))
        moves += 1
    return moves

T = int(input())
for t in range(1, T + 1):
    S, k = input().split(' ')
    S = list(map(lambda s: s == '+', S))
    k = int(k)
    result = oversized_pancake_flipper(S, k)
    if result == -1:
        result = 'IMPOSSIBLE'
    print('Case #{t}: {result}'.format(t=t, result=result))
