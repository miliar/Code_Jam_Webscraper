import bisect
import functools

def win(lsN,lsK):
    tbl = [[lsN[i],lsK[i]] for i in range(len(lsN))]
    return functools.reduce(lambda x,y : x and y[0]>y[1],tbl,True)

def ken(ls,Tnaomi):
    return ls.pop(bisect.bisect_right(ls,Tnaomi)%len(ls))

def naomiWar(ls):
    return ls.pop(0)

def naomiDWar(lsN,lsK):
    if win(lsN,lsK):
        told = lsN[-1]+0.000001*len(lsN)
        return lsN.pop(0), told
    else:
        return lsN.pop(0),lsK[-1]-0.000001

T=int(input())
for t in range(T):
    N=int(input())
    lNW = sorted([float(elt) for elt in input().split()])
    lKW = sorted([float(elt) for elt in input().split()])
    lNDW = lNW[:]
    lKDW = lKW[:]

    z=0
    for n in range(N):
        chosenNaomi =  naomiWar(lNW)
        z+= 1 if chosenNaomi > ken(lKW,chosenNaomi) else 0

    y=0
    for n in range(N):
        chosenNaomi, toldNaomi = naomiDWar(lNDW,lKDW)
        y+= 1 if chosenNaomi > ken(lKDW,toldNaomi) else 0

    print('Case #',t+1,': ',sep='',end='')
    print(y,z)
