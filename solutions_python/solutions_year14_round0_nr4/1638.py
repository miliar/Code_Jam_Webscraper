'''
	12/04/2014
	Google Code jam
	Problem 4: Deceitful War
'''

epsilon = 0.0000002

def solve(a, b, n):
	a.sort()
	b.sort()
	y=0
	j=0
	for i in range(n):
		if j<n and a[i]<b[j]:
			y+=1
			j+=1
		else:
			while j<n and a[i]>b[j]:
				j+=1
			if j==n:
				break
			else:
				y+=1
				j+=1
	y = n-y #naomi's score playing honest
	
	z=0
	i=n-1
	maxj=n-1
	minj=0
	while i>=0:
		while i>=0 and a[maxj] > b[i]: #blocks naomi wins
			z+=1
			i-=1
			maxj-=1
		while i>=0 and a[maxj] < b[i]: #blocks naomi loses
			minj+=1
			i-=1			
	
	return z, y
	
if __name__=='__main__':
	t = int( input() )
	for x in range(1, t+1):
		n = int(input())
		a = [float(x) for x in input().split()]
		b = [float(x) for x in input().split()]
			
		y, z = solve(a, b, n)
		print("Case #" + str(x) + ": " +str(y) +" "+str(z))