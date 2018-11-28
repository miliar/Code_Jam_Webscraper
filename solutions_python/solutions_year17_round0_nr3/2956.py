import re

def empty_stalls(occupied,j):
	i = j-1
	L = 0
	while i >= 0:
		if occupied[i] == 'o':
			break
		else:
			L = L + 1
			i = i - 1
		#end if
	#end while
	i = j+1
	R = 0
	while i < len(occupied):
		if occupied[i] == 'o':
			break
		else:
			i = i + 1
			R = R + 1
		#end if
	#end while
	return (j,L,R)

def sim(N,K):
	#print "N = {0} K = {1}".format(N,K)
	occupied = ['.']*(N+2)
	# guards occupy end stalls
	occupied[0] = 'o'
	occupied[N+1] = 'o'
	last_min_LR = None
	last_max_LR = None
	for i in xrange(K):
		#print "person ", i
		#print "".join(occupied)
		# computer L and R for a given stall s
		tups = []
		for s in xrange(1,N+1,1):
			if occupied[s] == '.':
				tups.append(empty_stalls(occupied,s))
			#end if
		#end
		#print tups
		max_min = None
		stalls = []
		for s in xrange(len(tups)):
			v = min(tups[s][1],tups[s][2])
			if max_min is None or v > max_min:
				max_min = v
			#end if
		#end 
		for s in xrange(len(tups)):
			v = min(tups[s][1],tups[s][2])
			if v == max_min:
				stalls.append((tups[s][0],s))
			#end if
		#end for
		#print "stalls: ", stalls
		max_max = None
		stalls2 = []
		for (_,s) in stalls:
			v = max(tups[s][1],tups[s][2])
			if max_max is None or v > max_max:
				max_max = v
			#end if
		#end
		for (_,s) in stalls:
			v = max(tups[s][1],tups[s][2])
			if v == max_max:
				stalls2.append((tups[s][0],s))
			#end if
		#end for
		#print "stalls2: ", stalls2
		if len(stalls) == 1:
			occupied[stalls[0][0]] = 'o'
			if i == K-1:
				t = tups[stalls[0][1]]
				#print t
				last_min_LR = min(t[1],t[2])
				last_max_LR = max(t[1],t[2])
			#end if
		else:
			occupied[stalls2[0][0]] = 'o'
			if i == K-1:
				t = tups[stalls2[0][1]]
				#print t
				last_min_LR = min(t[1],t[2])
				#print "last_min_LR: ", last_min_LR
				last_max_LR = max(t[1],t[2])
				#print "last_max_LR: ", last_max_LR
			#end if
		#end if
	#end for
	#print "".join(occupied)
	return (last_max_LR,last_min_LR)

if __name__ == "__main__":
	T = int(raw_input())
	for i in xrange(1,T+1,1):
		m = re.match(r'(\d+)\s(\d+)',raw_input())
		N = int(m.group(1))
		K = int(m.group(2))
		(y,z) = sim(N,K)
		print "Case #{0}: {1} {2}".format(i,y,z)
	#end for
#end if