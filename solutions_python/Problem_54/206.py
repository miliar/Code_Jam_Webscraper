import re,sys
fi=open("B-large.in")#"fair.in")#"B-small-attempt2.in")#


sys.stdout=open("fair.out","w")
C=int(fi.readline())
for c in range(C):
    t=re.sub("\s+$", "", fi.readline()).split()
    t=map(int,t)
    N=int(t[0])
    t=list(set(t[1:]))
    t.sort()
    rcnt=t[0]
    t=[ti-rcnt for ti in t[1:]]
    while len(t)>1:
        t=[t[0]]+[ti%t[0] for ti in t[1:]]
        t.sort()
        while t[0]==0:
            t=t[1:]
    T=t[0]
    ans=(-rcnt)%T
    print "Case #%i: %s"%(c+1,ans)

