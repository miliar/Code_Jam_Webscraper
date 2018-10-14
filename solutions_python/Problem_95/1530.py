a={}
a[' ']=' '
a['a']='y'
a['b']='h'
a['c']='e'
a['d']='s'
a['e']='o'
a['f']='c'
a['g']='v'
a['h']='x'
a['i']='d'
a['j']='u'
a['k']='i'
a['l']='g'
a['m']='l'
a['n']='b'
a['o']='k'
a['p']='r'
a['q']='z'
a['r']='t'
a['s']='n'
a['t']='w'
a['u']='j'
a['v']='p'
a['w']='f'
a['x']='m'
a['y']='a'
a['z']='q'
n=input()
for i in range(0,n):
	y=''
	x=raw_input()
	for j in range(0,len(x)):
		y+=a[x[j]]
	print 'Case #'+str(i+1)+': '+y
