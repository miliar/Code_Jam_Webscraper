def dict2(li, N, K, c):
	a = K
	b = N-1
	if a == b:
		if c < li[b]:
			return -1
		else:
			return K
	if c < li[b]:
		return -1
	elif c >= li[a]:
		return K 
	else:
		res = a 
		while res >= a  and res <= b-1:
			res = (a+b)/2
			if li[res] <= c:
				a = res
			else:
				b = res
		return res
			 


def solve():
	f = open("A-large.in.txt", 'r')
	#f = open("in.txt", 'r')
	T = int(f.readline())
	for t in range(T):
		[N,X] = [int(k) for k in f.readline().split()]
		weights = [int(k) for k in f.readline().split()]
		sortedWeights = sorted(weights,reverse=True)
		deja = [0 for k in range(N)]
		res = 0
		for i in range(N):
			if not deja[i]:
				res += 1
				deja[i] = 1
				for j in range(i+1, N):
					if sortedWeights[j] <= X - sortedWeights[i] and not deja[j]:
						deja[j] = 1
						break
		print "Case #%i:" % (t+1), res

solve()