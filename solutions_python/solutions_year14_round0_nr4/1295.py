#!/usr/bin/python3.2

filename = "D-large.in"

FILE = open(filename)
T = int(FILE.readline())


def get_fair(N, n, k):
    score = 0
    for i in range(0, N):
        naomi = n[i]
        if naomi > k[-1]:
            del k[0]
            score += 1
        else:
            for elem in k:
                if elem > naomi:
                    k.remove(elem)
                    break

    return score


for i in range(1,T+1):
    N = int(FILE.readline())
    naomi = sorted([float(x) for x in FILE.readline().split()])
    ken = sorted([float(x) for x in FILE.readline().split()])

    fair_wins = get_fair(N, naomi.copy(), ken.copy())
    unfair_wins = get_fair(N, ken.copy(), naomi.copy())

    print('Case #' + str(i) + ': ' + str(N - unfair_wins) + ' ' + str(fair_wins))

