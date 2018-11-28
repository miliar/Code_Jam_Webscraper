import re,sys
def _scans():
	while True:
		yield from input().split()
scans = _scans().__next__
scan = lambda: int(scans())
red = sys.stderr.write

sys.stdin = open('input.txt')
redir_out = 1

def tidy(x):
	x=str(x)
	return all(a<=b for a,b in zip(x,x[1:]))
def calc(n):
	l = 1
	for i in range(1,n+1):
		if tidy(i):
			l=i
	return l
def sel(n,i):
	try:
		return int(str(n)[-i-1])
	except:
		return 0
def calcf(n):
	for i in range(len(str(n))-1):
		a,b = sel(n,i+1),sel(n,i)
		if a>b:
			n-=(n%(10**(i+1))+1)
	return n

with open('output.txt','w') if redir_out else sys.stdout as sys.stdout:
	for t in range(scan()):
		red('%d\n'%(t+1))
		print('Case #%d: %d'%(t+1,calcf(scan())))