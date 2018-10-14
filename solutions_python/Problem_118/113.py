import bisect

def palin(s): return s == ''.join(s[::-1])

def getcombs(n,m):
    s = '0'*n
    for i in xrange(n):
        for j in xrange(i):
            for k in xrange(j):
                yield s[:k]+'1'+s[k+1:j]+'1'+s[j+1:i]+'1'+s[i+1:]
    for i in xrange(n):
        for j in xrange(i):
            yield s[:j]+'1'+s[j+1:i]+'1'+s[i+1:]
    for i in xrange(n):
        yield s[:i]+'1'+s[i+1:]
    yield s

def getfsq(hl):
    for c in getcombs(hl,1):
        cc = c
        for start in '12':
            c = start+cc
            rc=''.join(c[::-1])
            for i in ['']+map(str,xrange(3)):
                t = c+i+rc
                if palin(str(int(t)**2)):
                    yield int(t),int(t)**2

inpfile = open('C-large-2.in')

fairAndSquare = set([x[1] for hl in xrange(1,50)for x in getfsq(hl)])

fairAndSquare.update(set([i*i for i in xrange(1000)if palin(str(i)) and palin(str(i*i))]))

fairAndSquare = sorted(fairAndSquare)

f = open('q3out.txt','w')

for i,s in enumerate(list(inpfile)[1:]):
    a,b = map(int,s.split())
    f.write('Case #%d: %d\n'%(i+1,bisect.bisect_right(fairAndSquare, b)-bisect.bisect_left(fairAndSquare,a)))

f.close()
