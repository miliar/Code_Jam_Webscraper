#!/usr/bin/env python3

def playWar(naomi_o, ken_o):
    naomi = naomi_o.copy()
    ken = ken_o.copy()
    score_naomi = 0

    for w in reversed(naomi):
        kens_move = next((x for x in ken if x > w), None)
        if kens_move:
            ken.remove(kens_move)
        else:
            ken = ken[1:]
            score_naomi += 1

    return score_naomi

def playDeceitful(naomi_o, ken_o):
    naomi = naomi_o.copy()
    ken = ken_o.copy()
    score_naomi = 0

    while naomi:
        while naomi and naomi[0] < ken[0]:
            naomi = naomi[1:]
            ken = ken[:-1]

        while naomi and naomi[0] > ken[0]:
            score_naomi += 1
            naomi = naomi[1:]
            ken = ken[1:]

    return score_naomi

def solve():
    N = int(input().rstrip())
    naomi = sorted([float(x) for x in input().rstrip().split()])
    ken = sorted([float(x) for x in input().rstrip().split()])

    return (playDeceitful(naomi, ken), playWar(naomi, ken))

if __name__ == '__main__':
    T = int(input().rstrip())
    for i in range(1, T+1):
        dw, w = solve()
        print("Case #{}: {} {}".format(i, dw, w))
