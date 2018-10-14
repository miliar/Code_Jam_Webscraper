
known_in = """
y qee
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
z
"""

known_out = """
a zoo
our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up
q
"""

def translate(c):
    for i, o in zip(known_in, known_out):
        if i == c:
            return o

lookup = {' ': ' '}
for i in xrange(ord('a'), ord('z')+1):
    c = chr(i)
    lookup[c] = translate(c)

def solve(t):
    r = []
    for c in t:
        r.append(lookup[c])
    return ''.join(r)

T = int(raw_input())
for t in xrange(1, T+1):
    line = raw_input()
    solution = solve(line)
        
    print "Case #%d: %s" % (t, solution)
