import sys

f = sys.stdin

dict = {}
dict[' '] =  ' '
dict['a'] =  'y'
dict['b'] =  'h'
dict['c'] =  'e'
dict['d'] =  's'
dict['e'] =  'o'
dict['f'] =  'c'
dict['g'] =  'v'
dict['h'] =  'x'
dict['i'] =  'd'
dict['j'] =  'u'
dict['k'] =  'i'
dict['l'] =  'g'
dict['m'] =  'l'
dict['n'] =  'b'
dict['o'] =  'k'
dict['p'] =  'r'
dict['q'] =  'z'
dict['r'] =  't'
dict['s'] =  'n'
dict['t'] =  'w'
dict['u'] =  'j'
dict['v'] =  'p'
dict['w'] =  'f'
dict['x'] =  'm'
dict['y'] =  'a'
dict['z'] =  'q'

n = int(f.readline())


for i in range(1, n+1):
	print "Case #{}:".format(i),
	s1 = f.readline().rstrip()
	s2 = ""
	for c in range(len(s1)):
		s2 = s2 + dict[s1[c]]
	print s2


