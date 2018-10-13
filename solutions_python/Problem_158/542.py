finp=open('D-small-attempt2.in')
fout=open('Output.out','w')

def Valid(X,R,C):
    if (R*C)%X!=0:
        return False
    if X==1:
        return True
    if X>=7:
        return False
    if X<=2:
        return True
    if X==3 and R>1 and C>1:
        return True
    if X==4 and R>2 and C>2:
        return True
    if X==5 and R>2 and C>2:
        return True
    if X==6:
        if R>=6 or C>=6:
            if R>2 and C>2:
                return True
            else:
                return False
        else:
            return False

Inp=finp.read().split()
T=int(Inp[0])
for run in range(1,T+1):
    X=int(''.join(Inp[(3*run) - 2]))
    R=int(''.join(Inp[(3*run) - 1]))
    C=int(''.join(Inp[(3*run)]))
    Res=Valid(X,R,C)
    if Res:
        fout.write("Case #%d: GABRIEL\n" %run)
    else:
        fout.write("Case #%d: RICHARD\n" %run)
    run+=1
finp.close()
fout.close()
