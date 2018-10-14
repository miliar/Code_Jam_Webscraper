t=input()
def change(a):
    if a=="-":
        return "+"
    elif a=="+":
        return "-"
    a=anew
for i in range(t):
    pn=raw_input().split()
    p=list(pn[0])
    flip=int(pn[1])
    j=0
    ch=0
    while j<(len(p)-flip+1):
        if p[j]=="-":
            for k in range(flip):
                p[j+k]=change(p[j+k])
            ch+=1
        j+=1
    if p.count("-")==0:
        print "Case #%d: %d" %(i+1, ch)
    else:
        print "Case #%d: IMPOSSIBLE" %(i+1)

