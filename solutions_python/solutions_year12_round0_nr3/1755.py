#!/usr/bin/env python

def permute(s):
    if len(s) == 1:
        return [s]
    perms = []
    for ix,c in enumerate(s):
        for perm in permute(s[:ix] + s[ix+1:]):
            perms.append(c + perm)
    return perms

def cycles(s):
    s = str(s)
    return set([int(s[j:] + s[:j]) for j in xrange(len(s))])

def cycle(a, b):
    ss = [str(x) for x in xrange(a, b+1)]
    m = {}
    for s in ss:
        sd = list(s)
        sd.sort()
        sd = "".join(sd)
        m[sd] = m.get(sd, 0) + 1
    count = 0
    for k in sorted(m):
        combos = map(int,set(permute(k)))
        combos = list([i for i in combos if i >= a and i <= b])
        combos.sort()
        for i,s1 in enumerate(combos):
            c = cycles(s1)
            for s2 in combos[i+1:]:
                if s2 in c:
                    count += 1
    return count

def main(argv):
    import sys
    case = 0
    for line in sys.stdin:
        if case > 0:
            a,b = map(int, line.strip().split())
            print "Case #%d: %d" % (case, cycle(a,b))
        case += 1

main([])
