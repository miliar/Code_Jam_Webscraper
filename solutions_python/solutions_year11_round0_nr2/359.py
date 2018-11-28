def read(s):
    ww = s.split()
    c = int(ww.pop(0))
    combo = dict((w[:2], w[2]) for w in ww[:c])
    combo.update((w[1]+w[0], v) for w,v in combo.items())
    ww = ww[c:]
    c = int(ww.pop(0))
    assert len(ww) == c + 2
    oppo = set(ww[:c])
    invoke = ww[-1]
    return combo, oppo, invoke

def solve(combo, oppo, invoke):
    s = ''
    for e in invoke:
        s += e
        while s[-2:] in combo:
            s = s[:-2] + combo[s[-2:]]
        if any(a in s and b in s for a, b in oppo):
            s = ''
    return ', '.join(s)
    
def main(L):
    for t in range(1, 1 + int(L[0])):
        print 'Case #%d: [%s]' % (t, solve(*read(L[t])))

import sys
main(list(sys.stdin))
                                  
