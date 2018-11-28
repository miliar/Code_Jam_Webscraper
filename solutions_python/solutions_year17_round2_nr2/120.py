
import itertools


def build3(A, B, C, S):
    n = A - 1
    if n > B + C:
        return
    if B < C:
        B, C, S = C, B, S[0] + S[2] + S[1]
    b, c = min(B - C, n), 0
    n -= b
    if n:
        b, c = b + n / 2 + n % 2, c + n / 2
    return (S[0] + S[1]) * b + (S[0] + S[2]) * c + S[0]


def build2(A, B, S):
    if A < B:
        A, B, S = B, A, S[1] + S[0]
    n = A - 1
    if n > B:
        return
    return S * n + S[0]


def solve(N, R, O, Y, G, B, V):
    blocks = []
    if O:
        if B == O and N == B + O: return 'BO' * O
        B -= O + 1
        if B < 0: return
        blocks.append('BO' * O + 'B')
    if G:
        if R == G and N == R + G: return 'RG' * G
        R -= G + 1
        if R < 0: return
        blocks.append('RG' * G + 'R')
    if V:
        if Y == V and N == Y + V: return 'YV' * V
        Y -= V + 1
        if Y < 0: return
        blocks.append('YV' * V + 'Y')

    if R and Y and B:
        if R >= Y and R >= B:
            if R == Y + B and not blocks: return 'RY' * Y + 'RB' * B
            S = build3(R, Y, B, 'RYB')
        elif Y >= R and Y >= B:
            if Y == R + B and not blocks: return 'YR' * R + 'YB' * B
            S = build3(Y, R, B, 'YRB')
        else:
            if B == R + Y and not blocks: return 'BR' * R + 'BY' * Y
            S = build3(B, R, Y, 'BRY')
        if S is None:
            return
        blocks.append(S)
        R -= sum(int(c == 'R') for c in S)
        Y -= sum(int(c == 'Y') for c in S)
        B -= sum(int(c == 'B') for c in S)
        
    if R and Y:
        if R == Y and not blocks: return 'RY' * Y
        S = build2(R, Y, 'RY')
    elif R and B:
        if R == B and not blocks: return 'RB' * B
        S = build2(R, B, 'RB')
    elif Y and B:
        if Y == B and not blocks: return 'YB' * B
        S = build2(Y, B, 'YB')
    else:
        S = ''
    if S is None:
        return
    if S:
        blocks.append(S)
    R -= sum(int(c == 'R') for c in S)
    Y -= sum(int(c == 'Y') for c in S)
    B -= sum(int(c == 'B') for c in S)

    n = len(blocks)
    if R:
        if R > n: return
        blocks.extend(['R'] * R)
    if Y:
        if Y > n: return
        blocks.extend(['Y'] * Y)
    if B:
        if B > n: return
        blocks.extend(['B'] * B)

    n = len(blocks)
    for item in itertools.permutations(blocks):
        for i in xrange(n - 1):
            if item[i][-1] == item[i + 1][0]:
                break
        else:
            if item[n - 1][-1] != item[0][0]:
                return ''.join(item)
        

T = int(raw_input())
for t in xrange(T):
    N, R, O, Y, G, B, V = map(int, raw_input().split(' '))
    res = solve(N, R, O, Y, G, B, V)
    print 'Case #%d: %s' % (t + 1, res or 'IMPOSSIBLE')
