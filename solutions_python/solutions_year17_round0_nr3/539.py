import re,sys
def _scans():
	while True:
		yield from input().split()
scans = _scans().__next__
scan = lambda: int(scans())
red = sys.stderr.write

sys.stdin = open('input.txt')
redir_out = 1

def calc(n,k):
	s = [0]+[1]*n+[0]
	for _ in range(k):
		l = [-1]*(n+2)
		r = [-1]*(n+2)
		for i in range(n+2):
			if s[i]:
				l[i] = l[i-1]+1
			else :
				l[i] = -1
		for i in range(n+1,-1,-1):
			if s[i]:
				r[i] = r[i+1]+1
			else :
				r[i] = -1
		o = ((min(l[i],r[i]),max(l[i],r[i]),-i) for i in range(n+2))
		o = max(o)
		s[-o[2]] = 0
	return o[1],o[0]
from functools import lru_cache
@lru_cache(maxsize=None)
def calcf(n,k):
	if k == 1:
		return n//2,(n-1)//2
	if k == 2:
		return calcf(n//2,1)
	n-=1
	k-=1
	l = calcf(n//2,k//2)
	r = calcf(n-n//2,k-k//2)
	if l[1] != r[1]:
		if l[1] < r[1]:
			return l
		else:
			return r
	else:
		if l[0] < r[0]:
			return l
		else:
			return r

with open('output.txt','w') if redir_out else sys.stdout as sys.stdout:
	for t in range(scan()):
		red('%d\n'%(t+1))
		print('Case #%d: %d %d'%(t+1,*calcf(scan(),scan())))