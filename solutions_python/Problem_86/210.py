def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def lcmm(*args):
    return reduce(lcm, args)


fp = open('in')
T = int(fp.readline())

for t in range(T):
    N, L, H = map(int,fp.readline().split())
    F = list(map(int,fp.readline().split()))

    for i in range(L,H+1):
        b = True
        for f in F:
            current = (i%f == 0) or (f%i == 0)
            b = b and current
        if b == True:
            szam = str(i)
            break
        else:
            szam = 'NO'

    print "Case #%d:"%(t+1),szam
