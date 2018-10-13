def isTidy(n):
    prev=0
    for c in str(n):
        if int(c)<prev:
            return False
        prev=int(c)
    return True

def tidy(n):
    sn=list(str(n))
    for i in range(len(sn)-1):
        if int(sn[i])>int(sn[i+1]):
            sn[i]=str(int(sn[i])-1)
            for j in range(i+1,len(sn)):
                sn[j]='9'
    return int(''.join(sn))

fi=open('ex2-large.in')
fo=open('ex2-large.out','w')
print tidy(123273624)
nCases=int(fi.readline())
for case in range(1,nCases+1):
    n=int(fi.readline())
    while not isTidy(n):
        n=tidy(n)
    fo.write('Case #%s: %s\n' % (case,n))

fi.close()
fo.close()
