import heapq

#fin = open('C-small-1-attempt0.in', 'r')
fin = open('C-small-2-attempt1.in', 'r')
fout = open('output.txt', 'w')

t = int(fin.readline())

slow = 0

def bubble_last(q):
	l = len(q) - 1
	#c = 0
	while l > 0 and q[l] > q[l - 1]:
		temp = q[l - 1]
		q[l - 1] = q[l]
		q[l] = temp
		l -= 1
		#c += 1
	#if c > 1:
	#	print "A lot"
	

for c in xrange(t):
	n, k = map(int, fin.readline().split())
	
	if slow:
		print "SLOW"
	
		stalls = [0]*n
		left = [-1]*n
		right = [n]*n
		MinMax = -1
		MaxMax = -1
	
		for i in xrange(k):
			MinMax = -1
			MaxMax = -1
			stall = -1
			for j in xrange(n):
				if stalls[j] == 0:
					Ls = j - left[j] - 1
					Rs = right[j] - j - 1
					minn = min(Ls, Rs)
					maxx = max(Ls, Rs)
					if minn > MinMax or minn == MinMax and maxx > MaxMax:
						MinMax = minn
						MaxMax = maxx
						stall = j
			stalls[stall] = 1
			s = stall + 1
			while s < n and left[s] < stall:
				left[s] = stall
				s += 1
			s = stall - 1
			while s >= 0 and right[s] > stall:
				right[s] = stall
				s -= 1
					
		fout.write('Case #' + str(c + 1) + ': ' + str(MaxMax) + ' ' + str(MinMax) + '\n')

	else:
		q = [-1*n]
		heapq.heapify(q)
		maxx = 0
		minn = 0
		print c
		for i in xrange(k):
			#print q
			j = abs(heapq.heappop(q))
			maxx = j//2
			if j%2 == 0 and j <> 0:
				minn = maxx - 1
			else:
				minn = maxx
			
			heapq.heappush(q, -1*maxx)
			heapq.heappush(q, -1*minn)

		fout.write('Case #' + str(c + 1) + ': ' + str(maxx) + ' ' + str(minn) + '\n')

fout.close()

