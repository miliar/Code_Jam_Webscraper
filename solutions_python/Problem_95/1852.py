import sys

def main():
	i = sys.stdin.readline()
	s = sys.stdin.readlines()
	a = {}
	t = 1
	a[' '] = ' '
	a['a'] = 'y'
	a['c'] = 'e'
	a['b'] = 'h'
	a['e'] = 'o'
	a['d'] = 's'
	a['g'] = 'v'
	a['f'] = 'c'
	a['i'] = 'd'
	a['h'] = 'x'
	a['k'] = 'i'
	a['j'] = 'u'
	a['m'] = 'l'
	a['l'] = 'g'
	a['o'] = 'k'
	a['n'] = 'b'
	a['p'] = 'r'
	a['s'] = 'n'
	a['r'] = 't'
	a['u'] = 'j'
	a['t'] = 'w'
	a['w'] = 'f'
	a['v'] = 'p'
	a['y'] = 'a'
	a['x'] = 'm'
	a['z'] = 'q'
	a['q'] = 'z'
	for i in s:
		y = ''
		i = i.replace('\n','')
		for j in i:
			y = y+a[j]
		r = "Case #"+str(t)+": "+y
		t += 1
		print r

main()
