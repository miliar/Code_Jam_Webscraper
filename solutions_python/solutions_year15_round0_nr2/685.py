
def test(cakelist):
    minstep=max(cakelist)
    maxcake=minstep
    for i in range(1,maxcake):
        steps=i
        for j in range(0,len(cakelist)):
            if cakelist[j]>i:
                if cakelist[j]%i==0:
                    steps+=cakelist[j]/i-1
                else:
                    steps+=cakelist[j]/i
        if minstep>steps:
            minstep=steps
    return minstep
    
f=open("B-large.in")
allcount=int(f.readline().strip())

for i in range(0,allcount):
    usercount=int(f.readline().strip())
    cakelist=[int(cakecount) for cakecount in f.readline().strip().split()]
    result=test(cakelist)
    print "Case #%d: %d"%(i+1,result)
