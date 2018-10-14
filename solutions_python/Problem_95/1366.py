mapping = {}

mapping['y'] = 'a'
mapping['n'] = 'b'
mapping['f'] = 'c'
mapping['i'] = 'd'
mapping['c'] = 'e'
mapping['w'] = 'f'
mapping['l'] = 'g'
mapping['b'] = 'h'
mapping['k'] = 'i'
mapping['u'] = 'j'
mapping['o'] = 'k'
mapping['m'] = 'l'
mapping['x'] = 'm'
mapping['s'] = 'n'
mapping['e'] = 'o'
mapping['v'] = 'p'
mapping['z'] = 'q'
mapping['p'] = 'r'
mapping['d'] = 's'
mapping['r'] = 't'
mapping['j'] = 'u'
mapping['g'] = 'v'
mapping['t'] = 'w'
mapping['h'] = 'x'
mapping['a'] = 'y'
mapping['q'] = 'z'
mapping[' '] = ' '

f = open('q1.in', 'r')
n = int(f.readline().strip())
for i in xrange(0, n):
    line = f.readline().strip()
    out = 'Case #%d: ' % (i+1)
    for l in line:
        out += mapping[l]
    print out



