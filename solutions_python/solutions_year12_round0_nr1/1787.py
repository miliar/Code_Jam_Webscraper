l={}
l['e']='o'
l['j']='u'
l['p']='r'
l['m']='l'
l['y']='a'
l['s']='n'
l['l']='g'
#l['c']='e'
l['k']='i'
l['d']='s'
l['x']='m'
l['v']='p'
l['n']='b'
#l['m']='l'
l['c']='e'
l['r']='t'
l['i']='d'
l['r']='t'
l['b']='h'
l['t']='w'
l['a']='y'
l['f']='c'
l['g']='v'
l['h']='x'
l['o']='k'
l['q']='z'
l['u']='j'
l['w']='f'
l['z']='q'
l[' ']=' '


x=input()
for i in xrange(0,x):
	y=raw_input()
	y=list(y)
	for z in xrange(0,len(y)):
		y[z]=l[y[z]]
	y=''.join(y)
	print 'Case #'+str(i+1)+':', y



