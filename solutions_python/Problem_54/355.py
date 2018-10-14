f = open("B-large.in")
fOut = open("B-large.out", "w")

readIntVec = lambda f: [int(x) for x in f.readline().strip().split()]

def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a


T = int(f.readline().strip())

for tc in range(T):
    v = readIntVec(f)
    N = v[0]
    v = v[1:]

    
    T = abs(v[0] - v[1])
    for i in range(N):
        for j in range(i+1, N):
            T = gcd(T, abs(v[i] - v[j]))
       
    ans = T - v[0] % T

    if ans == T:
        ans = 0
            
    fOut.write("Case #%d: %d\n" % (tc + 1, ans))
    

fOut.close()
f.close()

