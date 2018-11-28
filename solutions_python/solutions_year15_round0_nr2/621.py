T = int(raw_input())


S = [[0]*1001 for i in range(1001)]
for i in range(1, 1001):
	for j in range(1, 1001):	
        	if j > i:
                	val = 2
                        while True:
                        	div = j/val
                                rem = j%val
                                if rem == 0:
                                	if div <= i:
                                        	S[i][j]= val-1
                                               	break
                                else:
                                        if div + 1 <= i:
                                                S[i][j] += val -1
                                                break
                                val += 1
	#print i
#print "here"
for t in range(T):
	D = int(raw_input())
	P = [int(i) for i in raw_input().split()]
	
	max_ = max(P)
	ans = max_
	for i in range(1, max_):
		count = 0
		for j in range(D):
			count += S[i][P[j]]
		#print i, count
		if  ans > i+count:
			ans = i + count
	print "Case #"+str(t+1)+": "+str(ans)
