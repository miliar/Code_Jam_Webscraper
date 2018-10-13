#(max(map(len,re.findall("R+", ln))+[0])>=K)
import re,sys
sys.stdout=open("rotate.out","w")

fi=open("A-large(2).in")#'rotate.in')#'A-small-attempt0(2).in')
T=int(fi.readline())
sps='.'*100
ans={0:"Neither",1:'Red',2:'Blue',3:'Both'}
for t in range(T):
    N,K=map(int,fi.readline().split()[:2])
    B,R=False,False
    dt=[]
    for i in range(N):
        ln=fi.readline()[:N].replace('.','')
        dt.append((sps+ln)[-N:])
    for ln in dt:
        B=B or re.search("B{%d}"%K, ln)!=None#(max(map(len,re.findall("B+", ln))+[0])>=K)
        R=R or re.search("R{%d}"%K, ln)!=None
    dtR=["".join([dt[j][i] for j in range(N)]) for i in range(N)]
    for ln in dtR:
        B=B or re.search("B{%d}"%K, ln)!=None
        R=R or re.search("R{%d}"%K, ln)!=None
    dtX=["".join([dt[i-j][j] for j in range(i+1)])+"#"+"".join([dt[N-i+j-1][N-j-1] for j in range(i+1)]) for i in range(N)]
    dtY=["".join([dt[N-1-i+j][j] for j in range(i+1)])+"#"+"".join([dt[i-j][N-j-1] for j in range(i+1)]) for i in range(N)]
    for ln in dtX:
        B=B or re.search("B{%d}"%K, ln)!=None
        R=R or re.search("R{%d}"%K, ln)!=None
    for ln in dtY:
        B=B or re.search("B{%d}"%K, ln)!=None
        R=R or re.search("R{%d}"%K, ln)!=None

    print "Case #%d: %s"%(t+1,ans[(B<<1)+R])
