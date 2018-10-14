import re, operator, string, time

def tobase(base, number):
	def tb(b,n,result=''):
		if n == 0: return result
		return tb(b,n/b,str(n%b)+result)

	if number < 2: return str(number)
	return tb(base, number)

def happy(n, base, no=[]):	
	if n==1 or n==base: return True
	if n in no: return False
	
	x=0
	s=tobase(base, n)	
	for c in s: x+=int(c)**2	
	
	if x==1 or x==base: return True
	
	no.append(n)
	return happy(x, base, no)

T=int(raw_input())

for case_no in range(1,T+1):
	bases=map(int, filter(bool, re.split("\s+", raw_input())))
	
	i=1
	while True:
		i+=1
		ok=True
		for b in bases:
			ok=ok and happy(i, b,[])
		if ok:
			print "Case #%d: %d" % (case_no, i)
			break
