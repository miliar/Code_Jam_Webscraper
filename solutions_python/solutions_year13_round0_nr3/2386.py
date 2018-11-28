#Python
def isPalind(n):
	tmp = str(n)
	if len(tmp) == 1:
		return 1
	s = 0
	e = len(tmp)-1
	while s < e:
		if tmp[s] != tmp[e]:
			return 0
		s += 1
		e -= 1
	return 1
	
if __name__=="__main__":
	N = int(raw_input())
	for i in range(N):
		r = 0
		vals = raw_input().split(' ')
		A = int(vals[0])
		s = int(pow(A,.5))
		B = int(vals[1])
		e = int(pow(B,.5))
		for j in range(s,e+1):
			t = isPalind(j)
			if t == 1:
				p = pow(j,2)
				if p < A:
					continue
				t = isPalind(p)
				if t == 1:
					r += 1
		print "Case #" + str(i+1) + ": " + str(r)
