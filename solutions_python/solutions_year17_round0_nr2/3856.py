import sys

def get_ans(sN):
	#print "sN:" + sN
	if len(sN) == 1:
		return sN
	idx = None
	for i in xrange(len(sN) - 1):
		#print "i:{}, i+1:{}".format(int(sN[i]),int (sN[i+1]))
		if int(sN[i]) > int (sN[i+1]):
			idx = i
			break
	if (idx == None):
		return sN

	#print 'gagabunga'
	#print sN[:idx+1]
	#print '0' * (len(sN) - idx - 1)
	newsN = str( int (sN[:idx + 1] + ('0' * (len(sN) - idx - 1))) - 1 )
	#print "newsN:" + newsN
	return get_ans(newsN)

T = int(sys.stdin.readline())

for k in xrange(T):
	sN = sys.stdin.readline()[:-1]
	
	ans = get_ans(sN)

	print "Case #{}: {}".format(k+1, ans)

