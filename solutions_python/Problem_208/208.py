#!/usr/bin/python3


def travel(D, ES0, ES):
    t = D[0]/ES0[1]
    ES0[0] -= D[0]
    if ES0[0] < 0:
        return -1, False
    t1, ok = get_min(D[1:], ES, ES0)
    return t+t1, ok


def get_min(D, ES, ES0):
    if not D:
        return 0, True
    if ES0[0] <= ES[0][0] and ES0[1] <= ES[0][1]:
        t1, ok1 = -1, False
    else:
        t1, ok1 = travel(D[:], ES0[:], ES[1:])
    if ES0[0] >= ES[0][0] and ES0[1] >= ES[0][1]:
        t2, ok2 = -1, False
    else:
        t2, ok2 = travel(D[:], ES[0][:], ES[1:])
        
    if not ok1:
        return t2, ok2
    if not ok2:
        return t1, ok1
    return min(t1, t2), True


T = int(input())


for t in range(T):
    
    N, Q = [int(x) for x in input().split()]

    ES = []
    for i in range(N):
        ES.append([int(x) for x in input().split()])

    D = []
    for i in range(N-1):
        D.append(int(input().split()[i+1]))
    input()
    input()
    
    
    x, ok = travel(D, ES[0], ES[1:])
    
    if not ok:
        raise RuntimeError(t+1)

    print("Case #{0}: {1}".format(t+1, x))


