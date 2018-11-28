import math
def ifSq(n):
    k=n
    n=str(n)
    if len(n)%2==1:
        n=n[:len(n)/2]+n[len(n)/2+1:]
    for i in range(len(n)/2):
        if not n[i]==n[len(n)-i-1]:
            return False
    return True
f=file("my2.txt","r")
lines=f.readlines()
n=int(lines[0])
lines=lines[1:]
lines=[x.replace("\n","").split(' ') for x in lines if not x=='\n']
res=[]
for i in range(n):
    k=0
    for j in range(int(math.pow(int(lines[i][0]),0.5)),int(math.pow(int(lines[i][1]),0.5))+1):
        if ifSq(j):
            m=j*j
            if m>int(lines[i][1]): 
                break
            if  m<int(lines[i][0]):
                continue
            if ifSq(m):
                k+=1
    res.append("Case #"+str(i+1)+": "+str(k))
f.close()
f=file("res.txt","w")
f.write("\n".join(res));
f.close()
