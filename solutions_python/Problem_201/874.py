import sys	

def calc(N, K):
	length = [N]
	cnt = {N:1}
	p = 0
	
	while True:
		l = length[p]
		c = cnt[l]
		K -= c
		p = p + 1
		
		maxLR = l/2
		minLR = (l-1)/2
		if K <= 0:
			return maxLR, minLR

		if maxLR not in cnt:
			length.append(maxLR)
			cnt[maxLR] = c
		else:
			cnt[maxLR] += c

		if minLR not in cnt:
			length.append(minLR)
			cnt[minLR] = c
		else:
			cnt[minLR] += c

if __name__ == "__main__":
	
	filename = "in.txt"
	if len(sys.argv) > 1:
		filename = sys.argv[1]	
 
	file = open(filename, 'r')
	T = int(file.readline())

	for id in xrange(1, T+1):
		N, K = list(map(int, file.readline().split()))
		maxLR, minLR = calc(N, K)
		print("Case #%d: %d %d" % (id, maxLR, minLR))
		