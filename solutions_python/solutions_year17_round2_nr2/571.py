import copy

def uni(N, R, O, Y, G, B, V):
    if R <= G:
        if R == G and R+G == N:
            return 'RG'*G
        elif R+G != 0:
            return 'IMPOSSIBLE'
    if Y <= V:
        if Y == V and Y+V == N:
            return 'YV'*V
        elif Y+V != 0:
            return 'IMPOSSIBLE'
    if B <= O:
        if B == O and B+O == N:
            return 'BO'*O
        elif B+O != 0:
            return 'IMPOSSIBLE'

    A = []

    if G:
        A.append('RG'*G + 'R')
        R -= G + 1
    if V:
        A.append('YV'*V + 'Y')
        Y -= V + 1
    if O:
        A.append('BO'*O + 'B')
        B -= O + 1

    if R+Y < B - 1: return 'IMPOSSIBLE'
    if R+B < Y - 1: return 'IMPOSSIBLE'
    if B+Y < R - 1: return 'IMPOSSIBLE'

    prim = [R, Y, B]
    names = ['R', 'Y', 'B']
    primString = []

    start = maxRYB(prim, 0)
    lastBiggest = maxRYB(prim, 0) - 1

    while any(prim):
        tempPrim = copy.copy(prim)
        tempPrim[lastBiggest] = 0
        biggest = lastBiggest = maxRYB(tempPrim, start)
        prim[biggest] -= 1
        primString.append(names[biggest])

    if not primString:
        return ''.join(A)
    if not A:
        if primString[0] == primString[-1]:
            return 'IMPOSSIBLE'
        else:
            return ''.join(primString)

    didFit = False

    for i in xrange(len(A)):
        if primString[0] != A[i-1][-1] and primString[-1] != A[i][0]:
            A.insert(i, ''.join(primString))
            didFit = True
            break

    if not didFit:
        return 'IMPOSSIBLE'

    return ''.join(A)


def maxRYB(prim, tie):
    R, Y, B = prim
    if R > B and R > Y:
        return 0
    if Y > R and Y > B:
        return 1
    if B > R and B > Y:
        return 2
    if tie == 0:
      if R >= B and R >= Y:
        return 0
    if tie == 1:
      if Y >= R and Y >= B:
        return 1
    if tie == 2:
      if B >= R and B >= Y:
        return 2
    if R >= B and R >= Y:
        return 0
    if Y >= R and Y >= B:
        return 1
    if B >= R and B >= Y:
        return 2



t = int(raw_input())

for x in xrange(1, t+1):
    N, R, O, Y, G, B, V = map(int, raw_input().split(' '))
    print 'Case #{}: {}'.format(x, uni(N, R, O, Y, G, B, V))