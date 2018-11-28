thefile = "A-large"
outputfile = open(thefile+".out", "w")

with open(thefile+".in") as f:
	ff = [[int(x) for x in line.split()] for line in f]

#with open(thefile+".in") as f:
#	ff = [[x for x in line.split()] for line in f]

def f(A,L):
	if L == []:
		return A, L
	L.sort()
	x = L[0]
	while L and x < A:
		L.pop(0)
		A = A + x
		if L:
			x = L[0]
	return A, L

def g(A,L):
	counter = 0
	while L:
		A = 2*A -1
		A, L = f(A,L)
		counter +=1
	return counter

def h(A,L):
	if A == 1:
		return len(L)
	B, K = f(A,L)
	if K == []:
		return 0
	x = len(K)
	ans = [x]
	if x > 1:
		for i in range(x):
			ans.append(i + g(B,K[:x-i]))
	return min(ans)
		
for i in range(1,ff[0][0]+1):
	A = ff[2*i-1][0]
	L = ff[2*i]
	ans = h(A,L)
	outputfile.write("Case #%i: %i\n" % (i, ans))
