from sets import Set

inp = 'B-large.in'
outp = 'out.out'
h = open(inp, 'r')
g = open(outp, 'w')
t = int(h.readline())
for a in range(t):
	z = h.readline().split(' ')
	c = float(z[0])
	f = float(z[1])
	x = float(z[2])
	rate = 2.0
	tox = x/rate
	tonextfarm = c/rate
	toxplus = x/(rate+f)
	total = 0.0
	while(tox > (tonextfarm+toxplus)):
		#buy another farm
		total = total + tonextfarm
		rate = rate+f
		tox = x/rate
		tonextfarm = c/rate
		toxplus = x/(rate+f)
	total = total + tox
	g.write('Case #'+str(a+1)+': '+str(total)+'\n')
