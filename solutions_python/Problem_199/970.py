
import math

    
def update(str1,j,k):
    for i in range(k):
        if str1[j+i]=="+":
            str1[j+i]="-"
        else:
            str1[j+i]="+"

g = open('output.txt', 'w')

f = open('A-large.in', 'r')

t= int(f.readline())
for i in range(t):
    s=f.readline().split()
    str1=list(s[0])
    k=int(s[1])
    res=0
    for j in range(len(str1)-k+1):
        if (str1[j]=="-"):
            res+=1
            update(str1,j,k)
            
    for j in range(k-1):
        if str1[len(str1)-1-j] != "+":
           res=-1
    if res!=-1:
        out="Case #"+str(i+1)+": "+ str(res)+"\n"
    else:
        out = "Case #"+str(i+1)+": IMPOSSIBLE\n"

    g.write(out)
g.close()
        

