def is_possible(dt, n, m):
	new = []
	for i in xrange(n):
		tmp = []
		for j in xrange(m):
			tmp.append(3)
		new.append(tmp)
	
	#first cut maxmize by row
	for i in xrange(n):
		mx = 0
		for j in xrange(m):
			mx = max(dt[i][j], mx)
		for j in xrange(m):
			new[i][j] = mx
			
	#second cut minimize by column
	for j in xrange(m):
		mn = 0
		for i in xrange(n):
			mn = max(dt[i][j], mn)
		for i in xrange(n):
			if(new[i][j]>mn): new[i][j] = mn
			
	return dt == new
	

if __name__ == '__main__':

	k = input()
	for i in xrange(k):
		inp = raw_input()
		arr = inp.split()
		n = int(arr[0])
		m = int(arr[1])
		data = []
		for j in xrange(n):
			tmp = []
			inp = raw_input()
			inp = inp.split()
			for z in xrange(m):
				tmp.append(int(inp[z]))
			data.append(tmp)
		res =is_possible(data, n , m)
		if res: print "Case #"+str(i+1)+": YES"
		else: print "Case #"+str(i+1)+": NO"