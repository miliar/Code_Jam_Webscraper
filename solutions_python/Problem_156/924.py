import heapq

def solveBrute(l):
	m = max(l)

	if m <= 3: 
		return m
	
	mCount = 0	
	for i in l:
		if i == m: mCount += 1
	if mCount >= m: 
		return m
	
	ans = m
	if m <= 8: return solve(l)
	else:
		
		for i in range(3, 5):
			l.remove(m)
			l.append(i)
			l.append(m-i)
			ans = min(ans, 1 + solveBrute(l))
			l.remove(i)
			l.remove(m-i)
			l.append(m)
			
		return ans

		
def solve(l):
	hash = {}
	for i in l:
		if i not in hash:
			hash[i] = 0
		hash[i] += 1
		
	
	h = []
	for i in l:
		heapq.heappush(h, -i)
	ans = 0
	m = -heapq.heappop(h)
	globalMin = m

	while (m not in (1,2, 3)):

		if hash[m] > m: return min(globalMin, ans + m)
		ans += 1
		
		half = int(round(m/2.0))
		otherHalf = m - half
		#sqrt = int(math.sqrt(m))
		#half = m - sqrt
		#otherHalf = sqrt
		#print "current m " + str(m) + " current ans " + str(ans)	
		#print half, otherHalf
		if half not in hash:
			hash[half] = 0
		hash[half] += 1
		if otherHalf not in hash:
			hash[otherHalf] = 0
		hash[otherHalf] += 1
		
		heapq.heappush(h, -half)
		heapq.heappush(h, -otherHalf)
		

		m = -heapq.heappop(h)
		globalMin = min(globalMin, ans + m)
		#print "globalMin is " + str(globalMin)
		#print hash
		#print h
	#print m
	
	if m == 1: return min(globalMin, ans + 1)
	if m == 2:
		return min(globalMin, ans + 2)
	if m == 3:
		return min(globalMin, ans + 3)
		
f = open("B-small-attempt5.in", 'r')
f2 = open("outputPancake5.txt", 'w')

t = int(f.readline())
for i in xrange(t):
	
	f.readline()
	me = f.readline().rstrip()
	s = "Case #"+ str(i+1) + ": "
	l = map(int, me.split())
	if i == t-1:
		f2.write(s+str(solveBrute(l)))
	else:
		f2.write(s+ str(solveBrute(l)) + '\n')
	#print me + " took " + str(solve(l))
	if solve(l) != solveBrute(l):
		print i+1, l, solve(l), solveBrute(l)
	
f.close()
f2.close()