
"""
3
---+-++- 3
+++++ 4
-+-+- 4
"""

def swich(c):
    if c == "-":
        return("+")
    elif c == "+":
        return("-")



n=int(input())

for nb in range(n):
    l,k=input().split()
    l=[c for c in l]
    k=int(k)
    #print(k)
    x=0
    for i in range(len(l)-k+1):
        #print("".join(l))
        if l[i]=="-":
            for j in range(i,i+k):
                l[j]=swich(l[j])
            x+=1
    possible=True
    #print("".join(l))
    for i in range(max(len(l)-k+1,0),len(l)):
        if l[i]=="-":
            possible=False

    print("Case #"+str(nb+1)+": "+(str(x) if possible else "IMPOSSIBLE"))
