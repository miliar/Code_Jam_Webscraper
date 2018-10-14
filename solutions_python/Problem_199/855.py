import sys	

def calc(S, K):
	cnt = 0
	SS = []
	l = len(S)
	for i in xrange(l):
		SS.append(1 if S[i]=='-' else 0)
	for i in xrange(l - K + 1):
		if SS[i] % 2 == 1:
			cnt += 1
			for j in xrange(i, i + K):
				SS[j] += 1
	for i in xrange(l - K, l):
		if SS[i] % 2 == 1:
			return "IMPOSSIBLE"
				
	return "%d" % cnt
	
if __name__ == "__main__":
	
	filename = "in.txt"
	if len(sys.argv) > 1:
		filename = sys.argv[1]	
 
	file = open(filename, 'r')
	T = int(file.readline())

	for id in xrange(1, T+1):
		S, K = file.readline().split()
		K = int(K)
		
		print("Case #%d: %s" % (id, calc(S, K)))
