import sys

fi=open('C-large.in')
sys.stdout=open("C-large.out","w")
T=int(fi.readline())
for t in range(T):
    N=int(fi.readline())
    C=map(int,fi.readline().split())
    bad=0
    mn=10e7
    for i in C:
        bad^=i
        mn=min(mn,i)
    print "Case #%s: %s"%(t+1, "NO" if bad else sum(C)-mn)
fi.close()