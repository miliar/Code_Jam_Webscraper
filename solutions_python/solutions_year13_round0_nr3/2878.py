#in1 = '/home/marshynov/Downloads/C-small-practice.in'
in1 = '/home/marshynov/Downloads/C-small-attempt0.in'
out1 = '/home/marshynov/Downloads/C-small-attempt0.OUT'
in_f = open(in1, 'r')
out_f = open(out1, 'w')
import math


def ispalindrome(word):
    if len(word) < 2: return True
    if word[0] != word[-1]: return False
    return ispalindrome(word[1:-1])	

def dostuff(inx,A,B):
	result = 0
	a = int(math.sqrt(A))
	if a*a<A:
		a += 1
	b = int(math.sqrt(B))
	#print '------',a,b

	i = a
	while i <= b :
	    if ispalindrome(str(i)):
			sqr = int(math.pow(i,2))
			#print 'sqr', sqr
			if ispalindrome(str(sqr)):
				result += 1	
			    	#print '_',i
	    i += 1
	
	return 'Case #{0}: {1}'.format(inx,result)

cases = int(in_f.readline())
#print(cases)
for inx in range(0,cases):
 ns = in_f.readline()
 nst = ns.split()
 res = dostuff(inx+1, int(nst[0]), int(nst[1]))
 out_f.write(res+'\n')
 print(res)
