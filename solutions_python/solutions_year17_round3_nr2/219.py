#!/usr/bin/python3

def solve():
    nc, nj = list(map(int, input().split()))
    acs, ace, ajs, aje = [0]*nc, [0]*nc, [0]*nj, [0]*nj
    for i in range(nc):
        acs[i], ace[i] = list(map(int, input().split()))
    for i in range(nj):
        ajs[i], aje[i] = list(map(int, input().split()))
    ac = sorted([(acs[i], ace[i]) for i in range(nc)], key=lambda tup: tup[0])
    aj = sorted([(ajs[i], aje[i]) for i in range(nj)], key=lambda tup: tup[0])

    if nc + nj <= 1:
        return 2
    if nc + nj == 2:
        if nc == 2:
            if ac[1][1]-ac[0][0] <= 720 or ac[1][0]-ac[0][1] >= 720:
                return 2
        if nj == 2:
            if aj[1][1]-aj[0][0] <= 720 or aj[1][0]-aj[0][1] >= 720:
                return 2
        if nc == 1 and nj == 1:
            return 2
    return 4

nn = int(input())
for t in range(nn):
    print('Case #{}: {}'.format(t+1, solve()))
