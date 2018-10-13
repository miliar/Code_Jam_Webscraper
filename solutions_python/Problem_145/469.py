def chk(p,gen):
	if gen > 40:
		return -1
	while p[0]/p[1] < 1:
		gen = gen + 1
		p[0] = p[0] * 2
	p[0] = p[0] - p[1]
	if p[0] != 0:
		retVal = chk(p,gen)
		if retVal < 0:
			return -1
	return gen

t = input()
for it in range(int(t)):
	p = input()
	p = p.split('/')
	p[0], p[1] = int(p[0]), int(p[1])
	gen = 0
	gen = chk(p,gen)
	if gen > 0:
		print("Case #",it+1,": ",gen,sep='')
	else:
		print("Case #",it+1,": impossible",sep='')
