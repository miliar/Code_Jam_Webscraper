T=int(input())
for case in range(1,T+1):
    tt=input().split(' ')
    C=float(tt[0])
    F=float(tt[1])
    X=float(tt[2])
    #print(C,F,X)
    if X<=C:
        #print("DB1")
        print("Case #%d: %.7f"%(case,X/2))
        continue
    Spd=2.0
    Time=0.0
    ANS=1E300
    while True:
        t=Time+X/Spd
        if t>ANS:
            print("Case #%d: %.7f"%(case,ANS))
            break
        ANS=t
        Time+=C/Spd
        Spd+=F
        
    
