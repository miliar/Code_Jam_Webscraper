def solve(N, R, O, Y, G, B, V):
    if N == 1:
        return (
            ('R' if R else '') +
            ('O' if O else '') +
            ('Y' if Y else '') +
            ('G' if G else '') +
            ('B' if B else '') +
            ('V' if V else ''))

    if B + O == N and B == O:
        return 'BO' * B
    if Y + V == N and Y == V:
        return 'YV' * Y
    if R + G == N and R == G:
        return 'RG' * R

    if B < O + 1 and O > 0:
        return 'IMPOSSIBLE'
    B0 = 'BO' * O + 'B'
    B -= O
    if Y < V + 1 and V > 0:
        return 'IMPOSSIBLE'
    Y0 = 'YV' * V + 'Y'
    Y -= V
    if R < G + 1 and G > 0:
        return 'IMPOSSIBLE'
    R0 = 'RG' * G + 'R'
    R -= G
    #print('R:', R, 'O:', O, 'Y:', Y, 'G:', G, 'B:', B, 'V:', V)
    #print('R:', R, '- Y:', Y, '- B:', B)

    if R >= B and R >= Y:
        o = ['R', 'B', 'Y']
        n = [R, B, Y]
    elif B >= R and B >= Y:
        o = ['B', 'Y', 'R']
        n = [B, Y, R]
    else:
        o = ['Y', 'R', 'B']
        n = [Y, R, B]

    if n[0] > n[1] + n[2]:
        return 'IMPOSSIBLE'

    r = ''
    for i in range(n[0]):
        r += o[0]
        if i < n[1]:
            r += o[1]
        if i >= n[0] - n[2]:
            r += o[2]

    return r.replace('B', B0, 1).replace('Y', Y0, 1).replace('R', R0, 1)

num_cases = int(input())
for c in range(num_cases):
    args = list(map(int, input().split()))
    r = solve(*args)
    valid = ['RY', 'YR', 'BR', 'RB', 'YB', 'BY', 'OB', 'BO', 'VY', 'YV', 'RG', 'GR']
    if r != 'IMPOSSIBLE':
        assert(len(r) == args[0])
        for i in range(len(r) - 1):
            assert r[i:i+2] in valid, '"{}" invalid: {}'.format(r, r[i:i+2])
        if len(r) > 1:
            assert r[0] != r[-1], r
    print('Case #{}: {}'.format(c + 1, r))
