'''
Created on 14.04.2012

@author: Freddy
'''
d = dict()
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
d['\n'] = ''

f = open('C:\Users\Freddy\Desktop\A-small-attempt0.in')

n = int(f.readline())

for i in range(n):
    l = f.readline()
    o = []
    for c in l:
        o.append(d[c])
    
    print str.format("Case #{0}: {1}", i+1, ''.join(o))
    

