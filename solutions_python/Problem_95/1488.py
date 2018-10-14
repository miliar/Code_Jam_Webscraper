f = open('a.txt')
m = {' ': ' ', '\n': ''}
for line in f.readlines():
    if len(line) < 3: m[line[0]] = line[0]
    else: m[line[0]] = line[2]
g = open('A-small-attempt1.in')
t = int(g.readline())
for _t in xrange(t):
    print 'Case #%d: %s' % (_t + 1, ''.join(map(lambda c:m[c], list(g.readline()))))
