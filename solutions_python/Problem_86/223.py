

def gcd(a,b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)


def gcd_all(ls):
    if len(ls)==1:
        return ls[0]
    else:
        g = gcd(ls[0],ls[1])
        for a in ls[2:]:
            g = gcd(g,a)
        return g

def lcm(a,b):
    g = gcd(a,b)
    return (a/g)*b

def lcm_all(ls):
    if len(ls)==1:
        return ls[0]
    else:
        l = lcm(ls[0],ls[1])
        for a in ls[2:]:
            l = lcm(l,a)
        return l

def solve_one(t):
    n,l,h = [int(s) for s in raw_input().strip().split()]
    freq = sorted([int(s) for s in raw_input().strip().split()])

    low = []
    high = freq

    candidates = []

    debug = False

    if debug:
        print candidates

    for i in range(n+1):
        if low!=[]:
            ll = lcm_all(low)
        else:
            ll = 1

        if high!=[]:
            gg = gcd_all(high)
        else:
            gg = ll

        if debug:
            print low, high

        if(high!=[]):
            low.append(high[0])
            high = high[1:]

        if debug:
            print ll,gg

        if ll > gg:
            continue

        if gg % ll != 0:
            continue

        rr = ((l+ll-1)/ll)*ll

        if debug:
            print 'rr =',rr

        while (rr >= l) and (rr <= h):
            if (i == n) or (gg % rr == 0):
                candidates.append(rr)
                break
            rr += ll
            if debug:
                print "next= ",rr

    if len(candidates)==0:
        print "Case #%d: NO" % t
    else:
        print "Case #%d: %d" %(t,min(candidates))

def main():
    tt = int(raw_input())
    for t in range(tt):
        solve_one(t+1)


if __name__=='__main__':
    main()

