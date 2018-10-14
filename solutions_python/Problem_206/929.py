t = int(input())
for z in range(t):
	d,n = map(int,input().split())
	speed = []
	for i in range(n):
		a = list(map(int,input().split()))
		speed.append((d*a[1])/(d-a[0]))

	print ("Case #%s: %s" %(z+1,min(speed)))
