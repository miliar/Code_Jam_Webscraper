import math
# pozicia, koniec?, farba, index, valid

def counting(x, recept):
    mi, ma = math.floor(float(x) / (1.1 * recept)), math.ceil(float(x)/ (0.9 * recept))
    mi = max(mi, 1)
    minimum = 100000000000
    maximum = -1
    for i in range(mi, ma+1):
        if (0.9 * recept <= float(x)/i) and (float(x)/i <= 1.1 * recept):
            minimum = min(minimum, i)
            maximum = max(maximum, i)
    return minimum, maximum



T = int(input())
for tid in range(T):
    S = -1
    count = 0
    N, P = [int(x) for x in input().split(' ')]
    R = [int(x) for x in input().split(' ')]
    Q = []
    body = []
    for i in range(N):
        a = [int(x) for x in input().split(' ')]
        a = sorted(a)
        S = max(S, math.ceil(a[-1] / (R[i] * 0.9)))
        Q.append(a)
        for j, x in enumerate(a):
            zac, kon = counting(x, R[i])
            if kon == -1:
                continue
            body.append((zac, 0, i, j, True))
            body.append((kon, 1, i, j, True))
    body = sorted(body)
    P = [0 for i in range(N)]
    K = [0 for i in range(N)]
    for i in range(len(body)):
        pozicia, koniec, farba, index, valid = body[i]
        if valid:
            if koniec == 0:
                P[farba] += 1
            else:
                if K[farba] == 0:
                    P[farba] -= 1
                else:
                    K[farba] -= 1
            vsetky = True
            for x in P:
                if x == 0:
                    vsetky = False
                    break
            if vsetky:
                for f, x in enumerate(P):
                    P[f] -= 1
                    K[f] += 1
                count += 1

    print('Case #{}: {}'.format(tid + 1, str(count)))
