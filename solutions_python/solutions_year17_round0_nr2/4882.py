from itertools import groupby

for Ti in range(int(input())):
    N=int(input())
    Ni=N
    Found=False
    while Found==False and Ni>0:
        Found=True
        LN=list(str(Ni))
        LNI=[x[0] for x in groupby(LN)]
        if len(LNI)!=1:
            if LNI[0]!=0:
                if sorted(LNI)!=LNI:
                    Found=False
                else:
                    Found=True
            else:
                Found=False
        else:
            Found=True
        if Found or Ni==1: #
            print("Case #"+str(Ti+1)+": "+str(Ni))
        Ni=Ni-1
