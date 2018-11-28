import sys
Print = sys.stdout.write
t=int(input())
for k in range(t):
	y=int(input())
	while y:
		list=[]
		x=y
		while x:
			list.insert(0,x%10)
			x/=10
		if list==sorted(list):
			print "Case #%d: %d"%(k+1,y)
			break
		y-=1