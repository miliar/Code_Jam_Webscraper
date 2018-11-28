def gcd (a, b):
    if b > a:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a

C = int(raw_input())

for case in range(1, C+1):
    ts = map(int, raw_input().split()[1:])
    T = 0
    for t in ts:
        T = gcd(abs(t-ts[0]), T)

    print 'Case #%i:' % case, (-ts[0])%T
