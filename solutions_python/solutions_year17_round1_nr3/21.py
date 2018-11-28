import sys

def isImpossible(Hd,Ad,Hk,Ak,B,D):
    if Ad>=Hk:
        print("win on first turn")
        return False # win on first turn
    if Ak-D>=Hd:
        print("lose on first turn")
        return True # lose on first turn
    if 2*Ad>=Hk or Ad+B>=Hk:
        print("win on second turn")
        return False # win on second turn
    if 2*Ak-3*D>=Hd:
        print("lose on second turn")
        return True #lose on second turn
    return False # it is possible to debuff the dragon down to 0.

def simulate(initialA,d,Hd,Ak,D):
    a = initialA
    H,A = Hd,Ak
    m=0
    while a>0 and m<2*initialA+100:
        m+=1
        if d>0:
            if H>(A-D):
                d-=1
                A-=D
                A = max(A,0)
            else:
                H = Hd
            H-=A
        else:
            if H>A or a==1:
                a-=1
            else:
                H = Hd
            H-=A
    return m

fileName = "C-small-attempt0"
sys.stdin = open(fileName+".in", 'r')
output = open(fileName+".out", 'w')
T = int(input())
for case in range(1,T+1):

    ###################### input data ###############################

    Hd,Ad,Hk,Ak,B,D = input().split(" ")
    print("Hd="+Hd+", Ad="+Ad+", Hk="+Hk+", Ak="+Ak+", B="+B+", D="+D)
    Hd,Ad,Hk,Ak,B,D = int(Hd),int(Ad),int(Hk),int(Ak),int(B),int(D)

    ################# check if it is impossible ##########################

    if isImpossible(Hd,Ad,Hk,Ak,B,D):
        answer = "IMPOSSIBLE"
        ######################## create output file ###############################
        print("Case #%d:" % case, answer)
        print("Case #%d:" % case, answer, file = output)
        ###########################################################################
        continue

    ################# compute number of attack moves ##########################

    a = (Hk-1)//Ad + 1
    if B>0:
        approx = int( ((Hk*B)**0.5-Ad)/B )
        bMin = max(0,approx-1000)
        bMax = approx+1000
        bBest = approx
        namBest = 2*Hk+100
        for b in range(bMin,bMax):
            nam = b + (Hk-1)//(Ad+b*B) + 1
            if nam<namBest:
                bBest,namBest = b,nam
        a = namBest
    print("a = "+str(a))

    ################# iterate over the number of debuff moves ########################

    m = simulate(a,0,Hd,Ak,D)
    if D>0:
        dMin=0
        dMax=Ak//D+1
        while dMax-dMin>20:
            cMin = int((2*dMin+dMax)//3)
            cMax = int((dMin+2*dMax)//3)
            m1 = simulate(a,cMin,Hd,Ak,D)
            m2 = simulate(a,cMax,Hd,Ak,D)
            if m1>m2:
                dMin = cMin
            else:
                dMax = cMax
        for d in range(dMin,dMax+1):
            x = simulate(a,d,Hd,Ak,D)
            if x<m:
                m=x
    answer = str(m)

    ######################## create output file ###############################
    print("Case #%d:" % case, answer)
    print("Case #%d:" % case, answer, file = output)
    ###########################################################################
