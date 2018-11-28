import string

infile = open('a.in','r')
outfile = open('a.out','w')

T = int(string.strip(infile.readline()))    

d = {}
d['a'] = 'y'
d['b'] = 'h'
d['c'] = 'e'
d['d'] = 's'
d['e'] = 'o'
d['f'] = 'c'
d['g'] = 'v'
d['h'] = 'x'
d['i'] = 'd'
d['j'] = 'u'
d['k'] = 'i'
d['l'] = 'g'
d['m'] = 'l'
d['n'] = 'b'
d['o'] = 'k'
d['p'] = 'r'
d['q'] = 'z'
d['r'] = 't'
d['s'] = 'n'
d['t'] = 'w'
d['u'] = 'j'
d['v'] = 'p'
d['w'] = 'f'
d['x'] = 'm'
d['y'] = 'a'
d['z'] = 'q'
d[' '] = ' '



for k in xrange(T):
    answer = ""
    s = string.strip(infile.readline())
    for i in s:
        answer += d[i]
    outfile.write('Case #%d: %s\n' % (k+1,answer))

