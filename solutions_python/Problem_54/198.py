
def FairWarning():
    tt = map(int, raw_input().split())[1:]
    T = 0
    for i in xrange(1, len(tt)):
        T = gcd(abs(tt[i]-tt[0]), T)
    y = 0
    for t in tt:
        m = t % T
        if m:
            y = max(y, T - m)
    print y

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

#---------------------------------------------------------------

C = int(raw_input())
for testcase in range(C):
    print "Case #%d:" % (testcase+1),
    FairWarning()
