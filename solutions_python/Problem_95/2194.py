import sys

map = {}
map['y']='a'
map['n']='b'
map['f']='c'
map['i']='d'
map['c']='e'
map['w']='f'
map['l']='g'
map['b']='h'
map['k']='i'
map['u']='j'
map['o']='k'
map['m']='l'
map['x']='m'
map['s']='n'
map['e']='o'
map['v']='p'
map['z']='q'
map['p']='r'
map['d']='s'
map['r']='t'
map['j']='u'
map['g']='v'
map['t']='w'
map['h']='x'
map['a']='y'
map['q']='z'
map[' ']=' '
f = open(sys.argv[1], 'r')
line = f.readline()
count = int(line)
i=0
while(i<count):
	newline = ''
	line = f.readline()
	for char in line:
		if char == '\n':
			break
		newline = newline + map[char]	
	print "Case #"+str((i+1))+": "+newline
	i=i+1