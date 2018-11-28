import sys
import fileinput

def primes(n): 
	if n==2: return [2]
	elif n<2: return []
	s=range(3,n+1,2)
	mroot = n ** 0.5
	half=(n+1)/2-1
	i=0
	m=3
	while m <= mroot:
		if s[i]:
			j=(m*m-3)/2
			s[j]=0
			while j<half:
				s[j]=0
				j+=m
		i=i+1
		m=2*i+3
	return [2]+[x for x in s if x]

p = primes(1000)

# returns primes >= P
def get_primes(P, M):
    return filter(lambda x: x >= P and x <= M, p) 

def solve(A, B, P):
    vals = {}
    for i in range(A, B+1):
        vals[i] = i

    ps = get_primes(P, B)
    for i in range(0, len(ps)):
        prime = ps[i]
        t = prime
        k = prime
        while k <= B:
            if k >= A:
                if vals[k] != k:
                    t = vals[k]
                    break
            k += prime

        k = prime
        while k <= B:
            if k >= A:
                vals[k] = t
            k += prime

    return len(set(vals.values()))

if __name__ == '__main__':
    lines = fileinput.input(sys.argv[1])
    N = int(lines.readline())
    for i in range(1, N+1):
        (A, B, P) = map(int, lines.readline().split(' '))
        out = solve(A, B, P)
        
        print "Case #%d: %d" % (i, out)
