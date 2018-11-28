def wp_(r, omit):
    w = sum(1 for i, c in enumerate(r) if c == '1' and i != omit)
    l = sum(1 for i, c in enumerate(r) if c == '0' and i != omit)
    return float(w)/(l+w)

def avg(xs):
    return float(sum(xs))/len(xs)

def solve(table):
    T = len(table)

    def opps(i):
        return [j for j, c in enumerate(table[i]) if c in '01']

    wps = [wp_(r, -1) for r in table]
    owps = [avg([wp_(table[o], i) for o in opps(i)]) for i in range(T)]
    oowps = [avg([owps[o] for o in opps(i)]) for i in range(T)]
    rpis = [0.25 * wp + 0.50 * owp + 0.25 * oowp for wp, owp, oowp in zip(wps, owps, oowps)]
    return '\n'.join('%.09f' % rpi for rpi in rpis)
    
def main(L):
    i = 1
    for t in range(1, 1+int(L[0])):
        r = int(L[i])
        print 'Case #%d:\n%s' % (t, solve(L[i+1:i+1+r]))
        i += 1 + r

import sys
main(list(sys.stdin))
