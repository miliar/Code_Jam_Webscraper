
def tidy(N):
	if N==0:
		return '0'

	listy = [int(i) for i in N]
	length = len(listy)

	for i in xrange(length-1, 0, -1):
		if listy[i]<listy[i-1]:
			listy[i-1] -= 1
			for j in xrange(i, length):
				listy[j] = 9

	return ''.join(map(str, filter(lambda x : x>0, listy)))


T = int(raw_input())

for t in xrange(T):
	print 'Case #'+str(t+1)+': '+tidy(raw_input())