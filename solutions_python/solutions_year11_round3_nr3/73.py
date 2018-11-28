def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a % b)

def LCM(a, b):
    return (a*b) / GCD(a, b)

for case in xrange(int(raw_input())):
    ans = None
    N, L, H = map(int, raw_input().split())
    players = map(int, raw_input().split())

    for i in range(L, H+1):
        found = True
        for p in players:
            if p % i != 0 and i % p != 0:
                found = False
                break
        if found:
            ans = i
            break

    print 'Case #%d: %s' % (case+1, ans if ans is not None else "NO")
