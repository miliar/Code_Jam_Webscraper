import sys

def bs(s):
	return str(s) if s<=1 else bs(s>>1) + str(s&1)

def keystrokes(A, B, P):
	probs = []
	for i in xrange(2**A):
		prob = 1
		b = bs(i)
		bstr = '0'*(A-len(b)) + b
		for j,b in enumerate(bstr):
			if b=='0':
				prob *= P[j]
			else:
				prob *= 1 - P[j]
		probs.append(prob)

	case1 = (B-A+1)*probs[0]+(2*B-A+2)*(1-probs[0])
	case3 = B+2.0

	cases = [0.0]*A
	for i in xrange(1,A+1):
		cases[i-1] = (2*i+2*B-A+2)*(1-sum(probs[:2**i])) + (2*i+B-A+1)*sum(probs[:2**i])
	return min(case1,case3, min(cases))

if __name__=='__main__':
	f = open(sys.argv[1], 'r')
	T = int(f.readline()[:-1])
	for case_no in xrange(1, T + 1):
		A,B = map(int, f.readline()[:-1].split(' '))
		P = map(float, f.readline()[:-1].split(' '))
		K = keystrokes(A, B, P)
		print "Case #%s: %0.6f" % (case_no, K)
	
