import sys

if __name__ == "__main__":
	nb = int(sys.stdin.readline())
	cpt = 1
	
	while cpt <= nb:
		c, f, x = sys.stdin.readline().replace('\n', '').split(' ')
		g = 2.0
		c = float(c)
		f = float(f)
		x = float(x)
		res = x/g
		m = 0.0
		
		while True:
			if res > m+(c/g)+(x/(g+f)):
				res = m+(c/g)+(x/(g+f))
				m += (c/g)
				g += f
			else:
				break
		
		print 'Case #'+str(cpt)+': '+'%.7f'%res
		cpt += 1