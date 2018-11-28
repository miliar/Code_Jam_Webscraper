from math import log, ceil

def reduceFraction(P, Q):
    for i in range(2, P + 1):
        while P % i == 0 and Q % i == 0:
            P //= i
            Q //= i

    return (P, Q)

def isInteger(N):
    return float(int(N)) == N


T = int(input())
for x in range(1, T + 1):
    (P, Q) = tuple(map(int, input().split('/')))

    (P, Q) = reduceFraction(P, Q)

    if not isInteger(log(Q, 2)):
        print('Case #%d: impossible' % (x,))
        continue
    else:
        print('Case #%d:' % (x,), ceil(log(Q / P, 2)))
