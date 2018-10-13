def gcd(a, b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)

t = int(raw_input())
for case in range(1, t+1):
    n, l, h = map(int,raw_input().split())
    f = map(int,raw_input().split())
    for x in range(l, h+1):
        for y in f:
            if y%x!=0 and x%y!=0:
                break
        else:
            print "Case #%d: %d" % (case, x)
            break
    else:
        print "Case #%d: NO" % case
