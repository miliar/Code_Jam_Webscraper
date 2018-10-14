
def tidy(n):
	l = len(n)
	nines = l
	for i in range(l-2,-1,-1):
		if n[i] > n[i+1]:
			n[i] = str(int(n[i])-1)
			n[i+1] = '9'
			nines = i+1
	n[nines:] = '9'*(l-nines)
	return ''.join(n)


testcases = int(raw_input())
for tc in range(1,testcases+1):
	n = list(raw_input())
	res = tidy(n)
	print 'Case #%d: %s' % (tc, int(res)) 



            
