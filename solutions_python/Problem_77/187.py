import itertools

file = open("G.txt", "r").read(100000)

parts = file.split("\n")
n = int(parts.pop(0))

out = open("out.txt", 'w')

def calc(A):
	n = 0
	for x in range(0, len(A)):
		if x+1 != A[x]:
			n += 1
			A[x],A[A[x]-1] = A[A[x]-1],A[x]
	return n



for i in range(1,n+1):
	N = parts.pop(0)
	A = parts.pop(0)
	out.write("Case #%d: %.5f\n" % (i, calc(list(map(lambda x: int(x), A.split(" "))))))