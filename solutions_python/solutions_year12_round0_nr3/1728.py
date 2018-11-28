import sys

def find_recycled_pairs(A, B):
	num_digits = len(str(A))
	count_pairs = 0
	numbers = range(A, B+1)
	for n in numbers:
		for i in range(1, num_digits):
			sm = str(n)
			m = int(sm[i:] + sm[:i])
			if n < m and m in numbers:
				count_pairs += 1
	return count_pairs

f = open(sys.argv[1])
if f != None:
	T = int(f.readline())
	for t in range(1, T+1):
		A, B = [int(x) for x in f.readline().split(" ")]
		print "Case #%d:" % t, find_recycled_pairs(A, B)
	f.close()