def gcd(a,b):
    if b == 0: return a
    else: return gcd(b, a%b)

T = input()
for t in range(T):
    n, pd, pg = [int(i) for i in raw_input().split()]
    possible = True

    if pd < 100 and pg == 100: possible = False
    elif pd > 0 and pg == 0: possible = False

    minp = 100/gcd(100,pd)
    if minp > n: possible = False

    print 'Case #%d: %s' % (t+1, 'Possible' if possible else 'Broken')
