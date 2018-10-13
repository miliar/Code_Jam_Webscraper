from math import sqrt

def answer(m,n):
    count=0    
    for x in range(int(sqrt(m)),int(sqrt(n))+1):
        if m<=x*x<=n*n:
            if str(x)==str(x)[::-1]:
                if str(x*x)==str(x*x)[::-1]:
                    count+=1
    return count           

data="""3
1 4
10 120
100 1000"""

data=open("B-small-attempt0.in").read()

data=data.split('\n')

# output answer
f=open("C-small.out","w")
T=int(data[0])
for i in range(T):
    m,n=map(int,data[i+1].split())
    out="Case #%d: %d\n"%((i+1),answer(m,n))
    f.write(out)
    print out
f.close()    

    
