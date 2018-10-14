te=int(raw_input())
fl=0;
def flip(mn,kin,dr):
    num=len(mn);
    if co>num-dr:
        return False;
    for i in range(dr):
        if mn[kin+i]=='-':
            mn[kin+i]='+'
        else:
            mn[kin+i]='-'
        
for i in range(te):
    s=raw_input()
    m=s.split()
    siz=int(m[1])
    syms=list(m[0])
    fl=len(syms)
    ans=0;
    ck=-1;
    for co in range(fl):
        if syms[co]=='-':
            dude=flip(syms,co,siz)
            if dude==False:
                print "Case "+"#"+str(i+1)+": IMPOSSIBLE"
                ck=2;
                break;
            ans+=1;
    if ck!=2:
        print "Case "+"#"+str(i+1)+": "+str(ans)
