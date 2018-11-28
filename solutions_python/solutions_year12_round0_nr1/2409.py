l = {}

l['y'] = 'a'
l['n'] = 'b'
l['f'] = 'c'
l['i'] = 'd'
l['c'] = 'e'
l['w'] = 'f'
l['l'] = 'g'
l['b'] = 'h'
l['k'] = 'i'
l['u'] = 'j'
l['o'] = 'k'
l['m'] = 'l'
l['x'] = 'm'
l['s'] = 'n'
l['e'] = 'o'
l['v'] = 'p'
l['z'] = 'q'
l['p'] = 'r'
l['d'] = 's'
l['r'] = 't'
l['j'] = 'u'
l['g'] = 'v'
l['t'] = 'w'
l['h'] = 'x'
l['a'] = 'y'
l['q'] = 'z'
l[' '] = ' '
l['\n'] = '\n'

inp = open('A.in')
out = open('A.out','w')

cases = int(inp.readline())
for case in xrange(1,cases+1):
	googlese = inp.readline()
	english = "".join([l[ch] for ch in googlese])
	out.write("Case #"+str(case)+": "+english)
