import sys

rl = lambda: sys.stdin.readline().strip()

for c in range(int(rl())):
    #dict = {'a': 'y', 'o' : 'e', 'z' : 'q', ' ': ' '}
    dict = {' ' : ' '}
    dict['a'] = 'y'#
    dict['b'] = 'h'#
    dict['c'] = 'e'#
    dict['d'] = 's'#
    dict['e'] = 'o'#
    dict['f'] = 'c'#
    dict['g'] = 'v'#
    dict['h'] = 'x'#
    dict['i'] = 'd'#
    dict['j'] = 'u'#
    dict['k'] = 'i'#
    dict['l'] = 'g'#
    dict['m'] = 'l'#
    dict['n'] = 'b'#
    dict['o'] = 'k'#
    dict['p'] = 'r'#
    dict['q'] = 'z'
    dict['r'] = 't'#
    dict['s'] = 'n'#
    dict['t'] = 'w'#
    dict['u'] = 'j'#
    dict['v'] = 'p'#
    dict['w'] = 'f'#
    dict['x'] = 'm'#
    dict['y'] = 'a'#
    dict['z'] = 'q'
    
    ans = ''
    for letter in rl():
        ans += dict[letter]
        
    print 'Case #%d: %s' % (c+1, ans)