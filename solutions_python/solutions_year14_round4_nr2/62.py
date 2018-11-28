W = 0

def decide(a, b):
	global W
	p = W.index(min(W[a:b+1]))
	if p-a <= b-p:
		t = W[p]
		for i in range(p-a):
			W[p-i] = W[p-i-1]
		W[a] = t
		return 1, p-a
	else:
		t = W[p]
		for i in range(b-p):
			W[p+i] = W[p+i+1]
		W[b] = t
		return 0, b-p




def solve():
	global W
	f = open("B-large.in.txt", 'r')
	#f = open("in.txt", 'r')
	T = int(f.readline())
	for t in range(T):
		N = int(f.readline())
		W = [int(k) for k in f.readline().split()]
		a = 0
		b = N-1
		res = 0
		while a != b:
			first, inter = decide(a, b)
			res += inter
			if first:
				a += 1
			else:
				b -= 1
		print "Case #%i:" % (t+1), res

solve()

