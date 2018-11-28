# python 3.4 !!

#from functools import lru_cache
#@lru_cache(maxsize = None)

from math import floor, ceil

num_trials = int(input())

# please don't read this code. i'm not very proud of it...

def isLegal(Qi, Rj):
    numPackages = int(round(Qi/Rj))
    properAmount = numPackages * Rj
    return 9 * properAmount <= 10 * Qi and 10 * Qi <= 11 * properAmount

def legalLoHi(Qi, Rj):
    QR = Qi/Rj
    return [int(ceil(10/11*QR)), int(floor(10/9*QR))]

def lessThan(ls):
    return ls[0] <= ls[1]

def overlap(lo1,hi1,lo2,hi2):
    return lo1 <= lo2 <= hi1 or lo2 <= lo1 <= hi2

def compute():
    N, P = map(int, input().split())
    R = list(map(int, input().split()))

    Q = [[]] * N
    for i in range(0,N):
        Q[i] = sorted(list(map(int, input().split())))

    legal = [[]] * N        
    for i in range(0,N):
        legal[i] = list(map(lambda x: legalLoHi(x, R[i]), Q[i]))
        legal[i] = [x for x in legal[i] if lessThan(x)]
        if len(legal[i]) == 0:
            return 0

    size = [len(legal[i]) for i in range(0,N)]

    iii = [0] * N # indices

    lo = legal[0][0][0]
    hi = legal[0][0][1]

    #print(Q)
    #print(legal)
    #print(size)

    count = 0

    while True:
        for j in range(0,N):
            # start by getting rid of the small j's
            if legal[j][iii[j]][1] < lo:
                while (legal[j][iii[j]][1] < lo):
                    iii[j] += 1
                    if iii[j] >= size[j]:
                        return count # run out of j's, done

            # not elif!!
            if legal[j][iii[j]][0] > hi:
                lo = legal[j][iii[j]][0]
                hi = legal[j][iii[j]][1]
                break
            else: 
                lo = max(lo, legal[j][iii[j]][0])
                hi = min(hi, legal[j][iii[j]][1])
        else:
            # nice made it!!
            count += 1
            for j in range(0,N):
                iii[j] += 1
                if iii[j] >= size[j]:
                    return count # run out of j's, done


    return -1

for i in range (0, num_trials):
    print("Case #" + str(i+1) + ": " + str(compute()))
