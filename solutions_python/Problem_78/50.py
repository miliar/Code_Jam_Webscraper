
def gcd(x, y):
    if y != 0:
        return gcd(y, x%y)
    else: return x

def lcm(x, y):
    return x*y/gcd(x,y)

def period(x):
    return 100 / gcd(100, x)

def calc(N, PD, PG):

    if PG == 100 and PD != 100:
        return "Broken"
    if PG == 0 and PD != 0:
        return "Broken"

    perD = period(PD)
    if perD <= N: return "Possible"
    else: return "Broken"


T = int(raw_input())
for t in range(0, T):
    N, PD, PG = map(int, raw_input().split())
    print "Case #%d: %s" % (t+1, calc(N, PD, PG))
