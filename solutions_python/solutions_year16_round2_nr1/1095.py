
def g(s):
    NMAP = {'ZERO': '0', 'ONE': '1', 'TWO': '2', 'THREE': '3', 'FOUR': '4', 'FIVE': '5', 'SIX': '6', 'SEVEN': '7', 'EIGHT': '8', 'NINE': '9'}
    nlist = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']
    d = {}
    for i, c in enumerate(s):
        try:
            d[c].append(i)
        except KeyError:
            d[c] = [i]

    number = []
    N = []
    if 'G' in s:
        N.append('EIGHT')
    if 'X' in s:
        N.append('SIX')
    if 'U' in s:
        N.append('FOUR')
    if 'W' in s:
        N.append('TWO')
    if 'Z' in s:
        N.append('ZERO')

    for rest in nlist:
        if rest not in N:
            N.append(rest)

    for rep in N:
        try:
            if all([len(d[c]) >= rep.count(c) for c in rep]):
                m = min([len(d[c]) for c in rep])
                number.extend([NMAP[rep]]*m)
                for c in rep:
                    for _ in xrange(m):
                        d[c].pop(0)
        except KeyError:
            continue
    if any(d.values()):
        print [k for k, v in d.iteritems() if v]
    number.sort()
    return ''.join(number)





h = open('a_out.txt', 'w')
f1 = 'test.txt'
f2 = 'alarge.in'

with open(f2, 'r') as f:
    T = f.readline()
    for i, e in enumerate(f.readlines()):
        r = g(e.strip())
        print 'Case #%s: %s' %(i+1, r)
        h.write('Case #%s: %s\n' %(i+1, r))
