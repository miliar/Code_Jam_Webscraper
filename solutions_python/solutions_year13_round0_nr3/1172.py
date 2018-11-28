def read_ints():
    return map(int, raw_input().split())

def read_str():
    return raw_input()

def isqrt(n):
    r=0
    b=1
    while b <= n:
        b *= 4
    b = b//4
    while b != 0:
        if n >= r+b:
            n -= r+b
            r = r//2+b
        else:
            r //= 2
        b //= 4
    return r

def is_palyndrome(n):
    x=str(n)
    return x==x[::-1]

def fair():
    A,B = read_ints()
    m=0
    for i in range(isqrt(A),isqrt(B)+1):
        k = i*i
        if k>=A and is_palyndrome(i) and is_palyndrome(k):
            m += 1
    return str(m)

T=read_ints()[0]
for t in xrange(T):
    print "Case #%d: %s" %(t+1, fair())

