from fractions import Fraction
#f = file('a.in')
import sys
f = sys.stdin

def solve():
    N = int(f.readline())
    lines = [f.readline().strip() for i in range(N)]
    
    owp = []
    owpc = []
    for n in range(N):
        o = Fraction(0)
        cc = 0
        for m in range(N):
            if lines[n][m] == '.':
                continue
            x = sum(1 for i, a in enumerate(lines[m]) if a == '1' and i != n)
            c = sum(1 for i, a in enumerate(lines[m]) if a != '.' and i != n)
            cc += 1
            if c != 0:
                o += Fraction(x, c)
        if cc == 0:
            owp.append(Fraction(0))
        else:
            owp.append(o / cc)
    for n in range(N):
        wp = Fraction(sum(1 for a in lines[n] if a == '1'),
                      sum(1 for a in lines[n] if a != '.'))
        oowp = Fraction(0)
        c = 0
        for i, a in enumerate(owp):
            if lines[n][i] != '.':
                oowp += a
                c += 1

        if c != 0:
            oowp /= c
        else:
            oowp = Fraction(0)

        rpi = wp / 4 + owp[n] / 2 + oowp / 4
        print float(rpi)
        #print wp / 4.0 + owp[n] / (2.0 * owpc[n]) + oowp / 4.0

T = int(f.readline().strip())
for c in range(1, T+1):
    print 'Case #%d:' % c
    solve()
