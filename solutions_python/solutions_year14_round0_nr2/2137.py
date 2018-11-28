from fractions import Fraction

T = int(raw_input())
for t in range(T):
    print "Case #{0}:".format(t+1),
    c, f, x = [float(i) for i in raw_input().split()]
    tm = 0.0
    cf = 0.0
    while True:
        # no farm: wait tm+x/(2+cf*f)
        # farm: wait tm+c/(2+cf*f), buy, wait x/(2+(cf+1)*f)
        # if less time, add c/(2+cf*f) to tm, increment cf
        #print cf, x/(2.0+cf*f), c/(2.0+cf*f)+x/(2.0+(cf+1.0)*f)
        if x/(2.0+cf*f) > c/(2.0+cf*f)+x/(2.0+(cf+1.0)*f):
            tm += c/(2.0+cf*f)
            cf += 1.0
        else:
            break
    print "{0:.7f}".format(tm+x/(2.0+cf*f))
            