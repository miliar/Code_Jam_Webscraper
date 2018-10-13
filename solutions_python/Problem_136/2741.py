def time(t,cps, x):
	return t + x/cps

cases = int(raw_input())
for cas in range(cases):
	numbers = raw_input().split(' ')
	c,f,x = [float(x) for x in numbers]
	res = 0.0
	cps = 2.0
	while time(res,cps,x) > time(res+(c/cps),cps+f,x):
		res += float(c/cps)
		cps += f
	res += x/cps
	print "Case #"+ str(cas+1) + ": {0:.7f}".format(res)