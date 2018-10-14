def make_number(d, k):
	r = 0
	for i in range(k):
		r = r *10 + d
	return r

def solve(line):
	n = int(line)
	d = len(line)
	if n < 10:
		return line
	if make_number(1, d) > n:
		return  make_number(9, d-1)
	ans = line
	for i in range(d):
		if i == 0:
			continue

		if line[i] < line[i-1]:
			#print '0: ', line[i]
			#print '1: ', line[:i-1]
			#print '2: ', str( int(line[i-1])-1 )
			#print '3: ', str(make_number(9, d-i))
			ans = line[:i-1] + str( int(line[i-1])-1 ) + str(make_number(9, d-i))
			return solve(ans)
	return ans

tn = -1
with open("p.in", "r") as myfile:
	for line in myfile:
		line = line.strip()
		tn += 1
		if tn == 0:
			continue

		print 'Case #%s: %s' % (tn, solve(line))

		

