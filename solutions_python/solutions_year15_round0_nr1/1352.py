from sys import argv
if __name__ == "__main__":
	inf = open(argv[1], 'r')
	lines = inf.readlines()
	inf.close()
	ouf = open(argv[2], 'w')
	ntest = int(lines[0][:-1])
	for i in range(ntest):
		val = lines[i+1][:-1].split(' ')
		m = int(val[0])
		p = 0
		ans = 0
		for j in range(m+1):
			if p < j:
				ans += (j-p)
				p = j
			p += int(val[1][j])
		ouf.write('Case #'+str(i+1)+': '+str(ans)+'\n')
	ouf.close()