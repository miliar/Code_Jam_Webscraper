from sys import stdin

def solve():
	L = []

	R = []
	Rd = {}
	O = []
	
	l = stdin.readline().split()
	r = int(l[0])
	R = l[1:r+1]

	for a,b,c in R:
		Rd[a+b]=c
		Rd[b+a]=c

	l = l[r+1:]

	O = l[1:-2]
	
	S = l[-1]

	for c in S:
		L.append(c)
		while len(L)>=2 and L[-2]+L[-1] in Rd:
			L = L[:-2] + [Rd[L[-2]+L[-1]]]

		for a,b in O:
			if a in L and b in L:
				L = []

	return str(L).replace("'",'')

n, = map(int, stdin.readline().split())
for i in range(n):
	print "Case #{}: {}".format(i+1, solve())
