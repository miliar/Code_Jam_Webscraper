n=int(input())
for _n in range(n):
    s=input().split()
    mx=int(s[0])
    A=[int(x) for x in s[1]]
    sm=A[0]
    plus=0
    plpl=0
    for k in range(1,len(A)):
        plus = 0 if k-sm<=0 else k-sm
        plpl+=plus
        sm+=A[k]+plus
    print("Case #{}: {}".format(_n+1,plpl))
    
