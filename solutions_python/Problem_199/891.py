st="Case #{}: "
with open("A-large.in") as file:
    arr=file.readlines()
cases=int(arr[0])
for case in range(cases):
    flips=0
    counter=0 #Program's patience
    poss=True
    larr=arr[case+1].split()
    S=list(larr[0])
    l=len(S)
    Sstr=larr[0]
    K=int(larr[1])
    pl=0
    plo=-1
    pr=-1
    pro=0
    while "-" in S:
        if(pl<plo or pr>pro):
            counter+=1
        if(counter>=2):
            poss=False
            break
        if(S[pl]=="-"):
            if(pl+1+K<=l):
                for i in range(K):
                    if(S[pl+i]=="+"):
                        S[pl+i]="-"
                    else:
                        S[pl+i]="+"
                flips+=1
            
        if(S[pr]=="-"):
            if((l+pr)+1-K>=0):
                for i in range(K):
                    if(S[pr-i]=="+"):
                        S[pr-i]="-"
                    else:
                        S[pr-i]="+"
                flips+=1
        Sstr="".join(S)
        plo=pl
        pro=pr
        pl=Sstr.find("-")
        pr=Sstr.rfind("-")
            
    if(poss):   
        print(st.format(case+1)+str(flips))
    else:
        print(st.format(case+1)+"IMPOSSIBLE")

def all_happy(S) -> bool:
    return "-" not in S

def flip(K,S,start,left:bool) -> str:
    if left:
        j=1
    else:
        j=-1
    for i in range(K):
        if(S[start+i*j]=="+"):
            S[start+i*j]="-"
        else:
            S[start+i*j]="+"
