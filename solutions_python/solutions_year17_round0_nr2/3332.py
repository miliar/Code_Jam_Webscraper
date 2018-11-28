
def tidy(n_str):
    n=[]
    for c in n_str:
        n.append(int(c))
    s=""
    if len(n)==1:
        return str(n[0])
    j=0
    while n[j]<=n[j+1]:
        j+=1
        if j==len(n)-1:
            break
    if j == len(n)-1:
        for i in range(len(n)):
            s+=str(n[i])
        return s
    k=j-1
    while n[k]==n[k+1] and k>=0:
        k-=1

    for i in range (k+1):
        s+=str(n[i])
    if k>-1 or n[k+1]-1>0:
        s=s+str(n[k+1]-1)
    for i in range (len(n)-k-2):
        s+="9"

    return s
name="B-large"
f=open(name+".in","r")
t=int(f.readline().strip("\n"))
f2=open(name+".out","w")
for i in range(1,1+t):
    n=list(f.readline().strip("\n")) #list of digit of n

    f2.write("Case #"+str(i)+": "+tidy(n)+"\n")
f.close()
f2.close()


