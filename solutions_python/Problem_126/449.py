import sys

def test(k, n):
	l=0
	while l<len(k):
		while l<len(k)-n and k[l] in ['a','e','i','o','u']:
			l +=1
		c = n
		while c > 0 and l<len(k) and not k[l] in ['a','e','i','o','u']:
			c -= 1
			l +=1
		l+=1
		if c == 0:
			return True
	return False			 

def solve(s, n):
	nv = 0
	for i in range(len(s)):
		for j in range(len(s)-i-n+1):
			#print i,j
			k = s[i:i+j+n]
			#print k
			if test(k,n):
				#print len(s)-j-i-n+1
				nv += len(s)-j-i-n+1
				break
				
	return nv


if __name__ == "__main__":
	N = int(sys.stdin.readline().strip())

	for t in range(N):
		l = sys.stdin.readline().strip().split(" ")
		print "Case #{0}: {1}".format(t+1, solve(l[0], int(l[1])))