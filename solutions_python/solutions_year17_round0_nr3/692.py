#INTNOG
def do(n, k):
	dic_ = {n:1}
	que = set([n])
	while len(que) != 0:
		a = max(que) 
		que.remove(a)
		l,r = a/2, (a-1)/2
		if l not in dic_: dic_[l] = 0
		if r not in dic_: dic_[r] = 0
		#print dic_, a, l, r
		dic_[l] += dic_[a]
		dic_[r] += dic_[a]
		if l != 1 and l !=  0: 
			que.add(l)
		if r != 1 and r !=  0: 
			que.add(r)
	count = 0
	arr = sorted(list(dic_.iteritems()),key=lambda x: x[0], reverse=True)
	prev = n
	#print arr
	for (key, c) in arr:
		count+= c
		if count >= k:
			return (key-1)/2, key/2
	return (arr[-1][0]-1)/2, arr[-1][0]/2
T = int(raw_input())
for t in xrange(T):
	n, k = map(int, raw_input().split())
	M, m = do(n, k)
	print "Case #{0}: {1} {2}".format(t+1, m, M)
