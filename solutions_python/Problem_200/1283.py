# def isTidy(K):
# 	print K;
# 	for i in xrange(1, len(K)):
# 		if K[i] < K[i-1]:
# 			return False;
# 	return True;

def findFirst(L):
	for i in xrange(len(L)-1, 0, -1):
		if L[i] < L[i-1]:
			L[i-1] -= 1;
			L[i:] = [9] * (len(L) - i);
	return int(''.join(map(str,L)));


T = int(raw_input());
for i in xrange(T):
	N = int(raw_input());
	ans = findFirst(map(int, str(N)));
	print "Case #%d: %d" % (i + 1, ans);