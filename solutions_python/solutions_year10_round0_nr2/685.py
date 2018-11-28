def gcd(a,b):
    if a>b:
        return gcd(b,a)
    # a <= b
    if a==0:
        return b
    return gcd(b%a,a)

def solve(t):
    difs=[abs(t0-t1) for t0, t1 in zip(t[:-1], t[1:])]
    accum_gcd=0
    for d in difs:
        accum_gcd=gcd(d,accum_gcd)
    return (-t[0]) % accum_gcd

T=int(input())
for case in range(1,T+1):
    t = [int(w) for w in input().split()[1:]]
    print("Case #{0}: {1}".format(case, solve(t)))
