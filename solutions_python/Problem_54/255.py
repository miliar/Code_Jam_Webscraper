f = open('B-large.in', 'r')
w = open('B-large.out','w')
def gcd(a, b):
    if(a%b==0):
        return b
    else:
        return gcd(b,a%b)
t = int(f.readline())
for T in range(t):
    R = f.readline().split()
    n = int(R[0])
    a = list(range(1001))
    for i in range(n):
        a[i] = int(R[i+1])
    x = a[0]
    GCD = 0
    for i in range(n-1):
        if(a[i+1]>a[i]):
            a[i] = a[i+1]-a[i]
        else:
            a[i] = a[i] - a[i+1]
        if(a[i]>0):
            GCD = a[i]
    for i in range(n-1):
        if(a[i]>0):
            GCD = gcd(GCD,a[i])
    if(x%GCD==0):
        w.write("Case #{0}: 0\n".format(T+1))
    else:
        w.write("Case #{0}: {1}\n".format(T+1,GCD - (x%GCD)))
f.close()
w.close()

    
        
