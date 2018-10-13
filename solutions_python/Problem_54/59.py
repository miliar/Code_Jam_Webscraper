import sys
import operator

sys.setrecursionlimit(2000)

def readn(f, n):
	return [f.readline().rstrip('\n') for i in range(n)]

def gcd2(a,b):
	if a < b:
		tmp = a
		a = b
		b = tmp
	while b > 0:
		tmp = a % b
		a = b
		b = tmp
	return a
	
def gcd(l):
	if len(l) == 2: return gcd2(l[0],l[1])
	return gcd([gcd2(l[0],l[1])]+l[2:])
	
f = open("B-large.in", 'r')

test = int(f.readline())



for tt in range(test):
	l = list(map(int,f.readline().split()))
	N = l[0]
	l = sorted(l[1:])
	m = l[0]
	l = list(map(lambda x: x-m, l))	
	div = gcd(l)
	res = m % div
	
	if res == 0 : ans = 0
	else : ans = div - res
	
	print("Case #{0}: {1}".format(tt+1, ans))
	
f.close()