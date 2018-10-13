t = int(input())

def check(n):
    n=str(n)
    for i in range(1,len(n)):
        if n[i]<n[i-1]:return False
    return True
for i in range(1, t + 1):
    n = int(input())
    m=1
    while not check(n):
        n-=(n%(10**m)-n%(10**(m-1)))
        n-=10**(m-1)
        m+=1
    print("Case #{}: {}".format(i, n))
