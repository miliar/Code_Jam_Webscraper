import sys
f = sys.stdin

def pair(a, b):
    return min(a, b) + max(a, b)

t = int(f.next())
for case in xrange(t):
    line = iter(f.next().split())
    c = int(line.next())
    transforms = {}
    for _ in xrange(c):
        b1, b2, n = line.next()
        p = pair(b1, b2)
        transforms[p] = n
    d = int(line.next())
    opposes = set()
    for _ in xrange(d):
        p = pair(*line.next())
        opposes.add(p)
    n = int(line.next())
    word = line.next()
    es = {}
    result = []
    for this in word:
        last = result[-1] if result else ""
        if pair(last, this) in transforms:
            nb = transforms[pair(last, this)]
            # remove last
            es[last] -= 1
            if es[last] == 0:
                del es[last]
            result.pop()
            
            result.append(nb)
            es[nb] = 1 + es.get(nb, 0)
            continue
        clear = False
        for e in es:
            if pair(e, this) in opposes:
                es = {}
                result = []
                clear = True
                break
        if clear:
            continue
        result.append(this)
        es[this] = 1 + es.get(this, 0)
    print "Case #%d: [%s]" % (case+1, ", ".join(result))
