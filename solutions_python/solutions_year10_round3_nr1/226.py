fi=open("A-large.in")#")
import sys
sys.stdout=open("out.out",'w')
T=int(fi.readline())
for i in range(T):
    N=int(fi.readline())
    lst=[map(int,fi.readline().split()) for j in range(N)]
    cnt=0
    for j in range(N):
        for k in range(j+1,N):
            cnt+=(lst[k][0]>lst[j][0])==(lst[k][1]<lst[j][1])
    print "Case #%d: %d"%(i+1,cnt)
