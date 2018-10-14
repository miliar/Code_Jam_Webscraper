import re,sys
def _scans():
	while True:
		yield from input().split()
scans = _scans().__next__
scan = lambda: int(scans())
red = lambda *a,**kw:print(*a,**kw,file=sys.stderr)

def calc(p,l):
	o = 0
	n = len(l)
	d = [0]*p
	for i in l:
		d[i%p] += 1
	o += d[0]
	if p==2:
		o += (d[1]+p-1)//2
		return o
	if p==3:
		x = min(d[1],d[2])
		d[1] -= x
		d[2] -= x
		o += x
		o += (d[1]+d[2]+p-1)//3
		return o
	if p==4:
		tp = [(0,1,0,1),(0,0,2,0),(0,2,1,0),(0,0,1,2),(0,4,0,0),(0,0,0,4)]
		for i in tp:
			x = min(d[j]//i[j] for j in (1,2,3) if i[j])
			for j in (1,2,3):
				d[j] -= x*i[j]
			o += x
		if sum(d[1:]) > 0:
			o+=1
		# if sum(d[i]*i for i in (1,2,3)) >= 4:
		# 	red(d[1:])
		return o

'''
if True:
	'''
sys.stdin = open('input.txt')
with open('output.txt','w') as sys.stdout:#'''
	for t in range(scan()):
		red('Case #%d'%(t+1))
		n,p=scan(),scan()
		print('Case #%d: %s'%(t+1,calc(p,[scan() for i in range(n)])))