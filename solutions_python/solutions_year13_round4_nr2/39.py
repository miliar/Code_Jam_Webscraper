#!/usr/bin/python3
import sys

best_dict = dict()
# najboljsi dosezek pri zame najbolj ugodnem razporedu
def best_score(vseh_ekip, boljsih):
    vseh_ekip2 = vseh_ekip
    boljsih2 = boljsih
    if (vseh_ekip2, boljsih2) in best_dict:
        return best_dict[(vseh_ekip2, boljsih2)]
    slabsih = vseh_ekip - 1 - boljsih
    if slabsih == 0:
        return boljsih # ne morem zmagat
    boljsih_naprej = (boljsih + 1) // 2
    best_dict[(vseh_ekip2, boljsih2)] = best_score(vseh_ekip // 2, min(boljsih_naprej, vseh_ekip // 2 - 1))
    return best_dict[(vseh_ekip2, boljsih2)]

worst_dict = dict()
# najboljsi dosezek pri zame najbolj neugodnem razporedu
def worst_score(vseh_ekip, boljsih):
    vseh_ekip2 = vseh_ekip
    boljsih2 = boljsih
    if (vseh_ekip2, boljsih2) in worst_dict:
        return worst_dict[(vseh_ekip2, boljsih2)]
    slabsih = vseh_ekip - 1 - boljsih
    if boljsih == 0:
        return boljsih # ne morem zgubit
    boljsih -= 1
    # sem premagan od enega boljsega
    boljsih_naprej = boljsih // 2
    worst_dict[(vseh_ekip2, boljsih2)] = vseh_ekip // 2 + worst_score(vseh_ekip // 2, min(boljsih_naprej, vseh_ekip // 2 - 1))
    return worst_dict[(vseh_ekip2, boljsih2)]


# bisection
def solve(N, P):
    # print([worst_score(2**3, i)+1 for i in range(2**N)]) 
    gL = 0
    gH = 2**N-1
    while gL < gH:
        # print(gL, gH)
        mid = (gL + gH + 1) // 2
        bmid = worst_score(2**N, mid)+1
        if bmid <= P:
            gL = mid
        else:
            gH = mid-1
    mL = 0
    mH = 2**N-1
    while mL < mH:
        mid = (mL + mH + 1) // 2
        bmid = best_score(2**N, mid)+1
        if bmid <= P:
            mL = mid
        else:
            mH = mid-1
    return gL, mL

T = int(sys.stdin.readline())
caseNum = 0

while caseNum < T:
    caseNum += 1
    N, P = map(int, sys.stdin.readline().strip().split(' '))
    garant, mozno = solve(N, P)
    print("Case #{0}: {1} {2}".format(caseNum, garant, mozno))
