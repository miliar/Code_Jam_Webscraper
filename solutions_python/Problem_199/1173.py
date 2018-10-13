FLIP = {
    '+': '-',
    '-': '+'
}

T = int(raw_input())
for t in xrange(1, T + 1):
    S, K = raw_input().split(' ')
    S = list(S)
    K = int(K)

    num_moves = 0
    i = 0
    for i in xrange(len(S) - K + 1):
        if S[i] == '+':
            continue
        S[i:i + K] = [FLIP[s] for s in S[i:i + K]]
        num_moves += 1

    if '-' in S[i:]:
        num_moves = 'IMPOSSIBLE'

    print 'Case #{}: {}'.format(t, num_moves)
