import string
import math

ifile = open("B-large.in")
fs = ifile.read().split("\n")
ifile.close()

T = int(fs[0])

out = []

NMidx = 1
for t in range(0,T):
    L = int(fs[NMidx].split(" ")[0])
    P = int(fs[NMidx].split(" ")[1])
    C = int(fs[NMidx].split(" ")[2])
    
    temp=L
    cnt=-1
    while temp < P:
        temp*=C
        cnt+=1

    if cnt==0:
        res=0
    elif cnt==1:
        res=1
    elif cnt==2:
        res=2
    else:
        res = int(math.floor(math.log(cnt,2)))+1
    

    out.append("Case #"+str(t+1)+": "+str(res))
    NMidx+= 1


ofile = open("output.txt","w")
ofile.write(string.join(out,"\n"))
ofile.close()