def gcd(a, b):
    while b:
        (a, b) = (b, a%b)
    return a

c = int(raw_input())
for test in range(1, c+1):
    t = map(int, raw_input().split())[1:]
    t.sort()
    d = t[1]-t[0]
    for x in t[2:]:
        d = gcd(d, x-t[0])
    t = t[-1]
    x = (t+d-1)/d*d
    print "Case #%d: %d" % (test, x-t)
