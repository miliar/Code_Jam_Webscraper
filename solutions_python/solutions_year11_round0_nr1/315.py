import sys
fi=open('A-large.in')
sys.stdout=open("A-large.out","w")
T=int(fi.readline())
for tn in range(T):
    l=fi.readline().split()
    N=int(l[0])
    l=[(l[2*i+1],int(l[2*i+2])) for i in range(N)]
    p={'O':1,'B':1}
    t={'O':0,'B':0}
    for r,v in l:
        r1="O" if r=="B" else "B"
        t[r]=max(t[r]+abs(v-p[r])+1,t[r1]+1)
        p[r]=v
    print "Case #%d: %d"%(tn+1,max(t.values()))