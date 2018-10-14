from sys import argv
def search(left, m):
	#print m, left
	if m <= 3:
		return m

	tmp = []
	for i in range(m+1):
		tmp.append(left[i])
	tmpm = m
	#print 'path1'
	for i in range(1, m):
		tmp[i] = tmp[i+1]
	tmp[m] = 0
	ans1 = 1+search(tmp, m-1)
	ans = ans1

	tmp = []
	for i in range(m+1):
		tmp.append(left[i])
	m = tmpm
	for i in range(2, m/2+1):
		#print 'path2', i
		tmp[m] -= 1
		tmp[i] += 1
		tmp[m-i] += 1

		while tmp[m] == 0:
			m -= 1
		ans2 = 1+search(tmp, m)
		m = tmpm
		tmp[m] += 1
		tmp[i] -= 1
		tmp[m-i] -= 1
		
		ans = min(ans2, ans)
	#print 'back'
	return ans

if __name__ == "__main__":
	inf = open(argv[1], 'r')
	lines = inf.readlines()
	inf.close()
	ouf = open(argv[2], 'w')
	ntest = int(lines[0][:-1])
	for i in range(ntest):
		n = int(lines[i*2+1][:-1])
		sval = lines[i*2+2][:-1].split(' ')
		val = [int(v) for v in sval]
		m = max(val)
		left = [0]*(m+1)
		for v in val:
			left[v] += 1
		#print left
		ans = search(left, m)
		ouf.write('Case #'+str(i+1)+': '+str(ans)+'\n')
		print '-------------'
	ouf.close()