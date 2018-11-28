def solve(N,K):
	c = 1
	Nc = N
	while c <= K:
		Nc -= c
		c *= 2
	
	c = 1
	while c <= K:
		prevN = N
		N /= 2
		c*=2

	c/=2
	K = K - c + 1
	x = Nc-c*(2*N-1) if prevN%2!=0 else Nc-c*(2*N-2)
	return ((N,N) if x >= K else (N,N-1)) if prevN%2!=0 else ((N,N-1) if x>=K else (N-1,N-1))



if __name__ == '__main__':
	t = input()
	c = 1
	while c <= t:
		N,K = map(int, raw_input().split())
		print 'Case #{}: {} {}'.format(c,*solve(N,K))
		c+=1
