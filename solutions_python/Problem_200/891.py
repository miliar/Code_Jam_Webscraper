import sys	

def get_fail_point(N):
	order = 1
	last = 9
	while N > 0:
		if N % 10 > last:
			return order
		last = N % 10
		N /= 10
		order *= 10
	return -1

def calc(N):
	fail_point = get_fail_point(N)
	while fail_point != -1:
		N -= N % fail_point + 1
		fail_point = get_fail_point(N)
	return N;

if __name__ == "__main__":
	
	filename = "in.txt"
	if len(sys.argv) > 1:
		filename = sys.argv[1]	
 
	file = open(filename, 'r')
	T = int(file.readline())

	for id in xrange(1, T+1):
		N = int(file.readline())
		print("Case #%d: %d" % (id, calc(N)))
		