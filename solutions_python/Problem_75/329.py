from collections import defaultdict

if __name__ == '__main__':
    for caseno in xrange(int(raw_input())):
        comb = {}
        opp = defaultdict(list)

        ps = raw_input().split()
        p = 0

        C = int(ps[p])
        p += 1

        for c in xrange(C):
            a, b, c = ps[p]
            comb[(a, b)] = comb[(b, a)] = c
            p += 1

        O = int(ps[p])
        p += 1
        for o in xrange(O):
            a, b = ps[p]
            opp[a] += [b]
            opp[b] += [a]
            p += 1

        p += 1

        elems = ps[p]

        curr = []
        for e in elems:
            if curr and comb.get((curr[-1], e)):
                curr[-1] = comb[(curr[-1], e)]
            elif any(c in curr for c in opp[e]):
                curr = []
            else:
                curr += [e]

        print 'Case #%d: %s' % (caseno + 1, '[%s]' % (', '.join(curr)))
