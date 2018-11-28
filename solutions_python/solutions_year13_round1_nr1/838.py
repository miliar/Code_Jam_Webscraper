T = int(input())
for tc in range(1, T+1):
    (r, t) = tuple(int(x) for x in input().split())
##    i = 0
##    a = 2*r + 1
##    while t-a >= 0:
##        t -= a
##        a += 4
##        i += 1
    i = (int((4*r*r - 4*r + 8*t + 1)**0.5) - 2*r + 1 + 1)//4
    while i*2*r - 3*i + 2*i*(i+1) > t:
        i -= 1
    print("Case #%i: %i" % (tc, i))
