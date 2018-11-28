def srch(x,a):
	for i in range(len(a)):
		if a[i] > x: return i
	return 0
	
t = int(input())
for testcase in range(t):
	n = int(input()) 
	na = sorted(list(map(float, input().split())))
	ke = sorted(list(map(float, input().split())))
	na2 = na[:]
	ke2= ke[:]
	points = 0
	for it in range(n):
		ni = len(na)-1
		ki = srch(na[ni], ke)
		if na[ni]>ke[ki]: points+=1
		del na[ni]
		del ke[ki]
	points2 = 0
	for it in range(n):
		while(len(ke2)-1-points2>=0):
			if na2[len(na2)-1-points2]>ke2[len(ke2)-1-points2]:
				points2+=1
			else:
				del ke2[len(ke2)-1-points2]

	print("Case #" + str(testcase+1) + ": "+ str(points2) + " " + str(points))
