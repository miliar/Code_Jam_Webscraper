#!local/usr/python
import sys,string

def gcd(a,b):
	if b==0: return a
	return gcd(b,a%b)

s = list(string.split(sys.stdin.readline()))
test = int(s[0])
testNo = 0
while testNo<test:
	testNo+=1
	
	s = list(string.split(sys.stdin.readline()))
	n = int(s[0])
	lista = []
	temp = s[1:]
	for a in temp:
		lista.append(int(a))
	
	lista.sort()
	
	res = -1
	last = -1
	
	for a in lista:
		if last!=-1 and a!=last:
			if res == -1: res = a-last
			else: res = gcd(res, a-last)
		last = a
	
	wynik = res-lista[0]%res
	if wynik==res: wynik=0
	print "Case #%d: %d" % (testNo, wynik)
sys.exit(0)
