#!/usr/bin/python3

def solve():
    N, R, O, Y, G, B, V = list(map(int, input().split()))
    if (R+Y<B or R+B<Y or B+Y<R):
        return 'IMPOSSIBLE'
    d = B+Y+R - max(B,Y,R)*2
    if R >= Y and R >= B:
        return 'RBY'*d + 'RB'*(B-d) + 'RY'*(Y-d)
    if B >= Y and B >= R:
        return 'BYR'*d + 'BY'*(Y-d) + 'BR'*(R-d)
    if Y >= B and Y >= R:
        return 'YBR'*d + 'YB'*(B-d) + 'YR'*(R-d)

nn = int(input())
for t in range(nn):
    print('Case #{}: {}'.format(t+1, solve()))
