import itertools
import math

f1 = open("A-small-attempt0.in","r")
f2 = open("out.txt","w")

data = f1.readlines()
k = int((data[0].split())[0])
ind=1
for i in range(k):
    dim=data[ind].split()
    n=int(dim[0])
    k=int(dim[1])
    ind+=1
    pan = []
    for j in range(n):
        line=data[ind].split()
        x=int(line[0])
        y=int(line[1])
        pan.append([x,y])
        ind+=1
    p = sorted(pan, key = lambda p: p[0], reverse=True)
    comb= list(itertools.combinations(range(n), k))
    mx=0
    for c in comb:
        temp=p[c[0]][0]*p[c[0]][0]
        for j in range(k):
            temp=temp+2*p[c[j]][0]*p[c[j]][1]
        mx=max(temp,mx)
    mx*=math.pi
    f2.write("Case #"+str(i+1)+": "+str("{:.6f}".format(mx))+"\n")

f1.close()
f2.close()
