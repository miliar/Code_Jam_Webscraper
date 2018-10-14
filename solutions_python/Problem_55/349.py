import sys
import re

if __name__=="__main__":
	fp = sys.stdin
	s = fp.readline()
	times = int(s)
	for loop in range(0, times):
		print "Case #%d:" % (loop+1),
		s = fp.readline()
		ss = re.findall('\d+', s)
		r = int(ss[0])
		k = int(ss[1])

		n = int(ss[2])
		s = fp.readline()
		ss = re.findall('\d+', s)
		g = []
		for s0 in ss:
			g.append(int(s0))
		g = g + g

		cap = 0
		everybody = True
		for i in range(0, n):
			cap += g[i]
			if cap > k:
				everybody = False
				break
		
		if everybody:
			print r*cap
			continue
	
		cap -= g[i]

		nextPos = [i % n]
		money = [cap]
		for i in range(1, n):
			cap -= g[i-1]
			for j in range(nextPos[i-1] , 2*n):
				cap += g[j]
				if cap > k:
					break
			cap -= g[j]
			nextPos.append(j % n)
			money.append(cap)
		

		pos = 0
		ans = 0
		h = []
		for i in range(0, n):
			h.append(-1)

		earn = [0]
		i = 0 
		while True:
			i += 1
			ans += money[pos]
			earn.append(ans)
			pos = nextPos[pos]
			if (h[pos] > 0):
				p1 = h[pos]+1
				p2 = i+1
				earn.append(ans+money[pos])
				#print h
				#print p1
				#print p2
				#print earn
				first = earn[p1]
				second = earn[p2] - earn[p1]

				length = p2 - p1
				step = (r - p1) / length
				rest = (r - p1) % length
				third = earn[p1 + rest] - earn[p1]
				#print "%d %d %d %d " % (first, second, third, step)
				res = first + second * step +  third
				print res
				break
			h[pos] = i 




			


	

