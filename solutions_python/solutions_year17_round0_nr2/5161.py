T = int(input())
def check(x):
    x=str(x)
    for j in range(1, len(x)):
        if int(x[j])<int(x[j-1]):
            return False
    return True
for arb in range(T):
    n = int(input())
    found=False
    while found!=True:
        
        if check(n):
            found=True
            break
        n-=1

    print("Case #{0}: {1}".format(arb+1, n))
        
    
