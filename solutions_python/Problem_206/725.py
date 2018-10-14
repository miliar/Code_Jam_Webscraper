import math
f = open('input.in','r')
w = open('output.out','w')
t = int(f.readline())
for i in range(1,t+1):
	d,n=map(int,f.readline().split())
	temp = -1
	for x in range(0,n):
		p,s=map(int,f.readline().split())
		temp = max(temp,(d-p)/s)
	ans = d/temp
	w.write('Case #{}: {:.6f}\n'.format(i,round(ans,6)))
f.close()
w.close()

