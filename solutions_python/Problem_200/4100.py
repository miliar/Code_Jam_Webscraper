import sys
t=int(input())
for k in range(t):
    x=int(input())
    s=str(x)
    l=list(s)
    i=0
    while(i<len(l)-1):
        if(l[i]>l[i+1]):
            l[i]=str(int(l[i])-1)
            for j in range(i+1,len(l)):
                l[j]='9'
                i=0
        else:
            i=i+1
            continue
    s=''.join(l)
    a=int(s)
    print"case #{}: {}".format(k+1,a)
