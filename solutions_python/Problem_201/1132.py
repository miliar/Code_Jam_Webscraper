import math

def bathroom(N, K):
	if(N == K):
		return (0, 0)
	m = 0
	M = 0
	x = 2 ** int(math.log(K, 2))
	d = K - x
	if(N >= (x * 2) + d):
		M = (N - d) // (x * 2)
	if(N >= (x * 3) + d):
		m = (N - d - x) // (x * 2)
	return (M, m)


FILE_NAME = "C:\\users\\avivr\\desktop\\C-small-2-attempt0.in"
OUT_FILE_NAME = "C:\\users\\avivr\\desktop\\out.txt"

f = open(FILE_NAME)
fo = open(OUT_FILE_NAME, 'w')
n = int(f.readline())

for i in range(n):
	line = f.readline().strip().split()
	N = int(line[0])
	K = int(line[1])
	res = bathroom(N, K)
	fo.write("case #" + str(i + 1) + ": " + str(res[0]) + " " + str(res[1]) + "\n")
f.close()
fo.close()