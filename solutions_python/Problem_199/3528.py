import time
def flip(gg,c):
    gg=str(gg)
    i=gg.find('-')
    gg=list(gg)
    if c+i>len(gg):
        return -1
    for i in range(i,c+i):
        if gg[i]=='-':
            gg[i]='+'
        elif gg[i]=='+':
            gg[i]='-'
    return gg

Li=[]
ANS=0
a=raw_input()
a=int(a)

for u in range(a):
    b,c=raw_input().split(" ")
    first=1
    c=int(c)
    while True:
        if '-' not in b:
            if first==1:
                Li.append(0)
                x=-1
            break
        else:
            x=flip(b,c)
            first=0
            if x==-1:
                Li.append("IMPOSSIBLE")
                ANS=0
                break
            else:
                b=x
                b=''.join(b)
                ANS=ANS+1
    if x!=-1:
        Li.append(ANS)
        ANS=0
        
for ii in range(len(Li)):
    print "Case #{}: {} ".format(ii+1, str(Li[ii]))


        
