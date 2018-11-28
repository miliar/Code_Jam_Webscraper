from heapq import heappush, heappop

def adddict(d,n,t):
	try:
		d[n]+=t
	except:
		d[n]=t

def bathroom(n,k,ptr=0):
	d={n:1}
	s=0
	while True:
		cur=max(d.keys())
		right,left=(cur)//2,(cur-1)//2
		s+=d[cur]
		if s>=k:
			return '{} {}'.format(right,left)
		else:
			adddict(d,right,d[cur])
			adddict(d,left,d[cur])
			del d[cur]

f=open('C-large.in','r')
g=open('C-large.out','w')
for i in range(1,int(f.readline().strip())+1):
	print('Case #{}: {}'.format(i,bathroom(*map(int,f.readline().strip().split()))),file=g)