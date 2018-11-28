dict = {}
dict['a']='y'
dict['b']='h'
dict['c']='e'
dict['d']='s'
dict['e']='o'
dict['f']='c'
dict['g']='v'
dict['h']='x'
dict['i']='d'
dict['j']='u'
dict['k']='i'
dict['l']='g'
dict['m']='l'
dict['n']='b'
dict['o']='k'
dict['p']='r'
dict['q']='z'
dict['r']='t'
dict['s']='n'
dict['t']='w'
dict['u']='j'
dict['v']='p'
dict['w']='f'
dict['x']='m'
dict['y']='a'
dict['z']='q'
t = int ( raw_input() )
for i in range(t):
	s = raw_input()
	o=""
	for j in s:
		if ( dict.has_key( j.lower() ) ):
			if ( j.isupper() ):
				o += ( dict[ j.lower() ].upper() )
			else:
				o += dict[j]
		else:
			o += j
	print "Case #" + str(i+1) + ": " + o
