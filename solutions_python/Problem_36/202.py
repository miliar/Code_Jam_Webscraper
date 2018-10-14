
def cntm(s,str):
    subm=[]
    m=0
    ml=len(s)
    for i in str:
        for j in subm:
            l=len(j)
            if l<ml:
                next=s[l:][0]
                if next==i:
                    subm.append(j+next)
        if i==s[0]:
            subm.append(i)
    for j in subm:
        l=len(j)
        if l==ml:
            m+=1
    return m

cases=int(raw_input())
s="welcome to code jam"
for x in xrange(cases):
    ss=raw_input()
    print "Case #%i: %s"%(x+1,str(cntm(s,ss)%10000).zfill(4))
