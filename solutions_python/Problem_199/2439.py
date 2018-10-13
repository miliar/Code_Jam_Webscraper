
def flip(s, i, j):
	for x in range(i,j):
		s[x] = not s[x]
	return s

def numFlips(s, k):
	l = len(s)-k+1
	flips = 0

	for i in range(l):
		if not s[i]:
			s = flip(s, i, i+k)
			flips += 1
	for x in s[l:]:
		if not x:
			return 'IMPOSSIBLE'
	return flips


testcases = int(raw_input())
for tc in range(1,testcases+1):
	a,b = raw_input().split()
	a = a.replace('+','1')
	a = a.replace('-','0')
	k = int(b)
	s = [bool(int(x)) for x in a]
	res = numFlips(s, k)
	print 'Case #%d: %s' % (tc, res)




    
    

            
