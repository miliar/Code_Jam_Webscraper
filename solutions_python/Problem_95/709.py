from sys import stdin
# ejp mysljylc kd kxveddknmc re jsicpdrysi
# our language is impossible to understand

# rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
# there are twenty six factorial possibilities

# de kr kd eoya kw aej tysr re ujdr lkgc jv
# so it is okay if you want to just give up

M = {}
M[' '] = ' '
M['a'] = 'y'
M['b'] = 'h'
M['c'] = 'e'
M['d'] = 's'
M['e'] = 'o'
M['f'] = 'c'
M['g'] = 'v'
M['h'] = 'x'
M['i'] = 'd'
M['j'] = 'u'
M['k'] = 'i'
M['l'] = 'g'
M['m'] = 'l'
M['n'] = 'b'
M['o'] = 'k'
M['p'] = 'r'
M['q'] = 'z'
M['r'] = 't'
M['s'] = 'n'
M['t'] = 'w'
M['u'] = 'j'
M['v'] = 'p'
M['w'] = 'f'
M['x'] = 'm'
M['y'] = 'a'
M['z'] = 'q'
t = int(stdin.readline())
for case in range(1, t + 1):
    s = ''
    g = stdin.readline()
    for c in g:
        try:
            s += M[c]
        except KeyError:
            continue
    print "Case #%d: %s" %(case, s)
