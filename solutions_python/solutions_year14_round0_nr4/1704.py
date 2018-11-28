from sys import stdin,stdout
from bisect import bisect_left as bl
def war(a,b,n):
	c=0
	d=b
	for i in range(n):
		#print(i)
		m=1
		for j in range(len(d)):
			if d[j]>a[i]:
				m=0
				d.remove(d[j])
				break
		if m==1:
			c+=1
			d.remove(d[0])

	return c
def deceitful_war(a,b,n):
	c=0
	i,j=0,0
	while (j<n and i<n ):
		if a[j]>b[i]:
			c+=1
			j+=1
			i+=1
		else:
			j+=1


	return c

for t in range(int(stdin.readline())):
	n = int(stdin.readline())
	blocks_naomi=list(map(float,stdin.readline().split()))
	blocks_ken = list(map(float,stdin.readline().split()))
	blocks_ken.sort()
	blocks_naomi.sort()
	

	print('Case #'+str(t+1)+': '+str(deceitful_war(blocks_naomi,blocks_ken,n))+' '+str(war(blocks_naomi,blocks_ken,n)))
	
