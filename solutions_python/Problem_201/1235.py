import numpy as np

t = int(input())
for i in range(t):
	xx = input().split()
	n = int(xx[0])
	k = int(xx[1])

	left = int(n/2)
	right = n - int(n/2) - 1
	countleft = 1
	countright = 1
	count = 0
	countk = 1
	while countk < k:
		# print("countk", countk + 2**count)
		if countk + 2**count > k:
			break
		countk += 2**count
		count += 1
		
		# tmp = max(int(left/2),left-int(left/2)-1,int(right/2),right-int(right/2)-1)
		t1 = max(int(left/2),left-int(left/2)-1,int(right/2),right-int(right/2)-1)
		t2 = min(int(left/2),left-int(left/2)-1,int(right/2),right-int(right/2)-1)
		c1 = 0
		c2 = 0
		if int(left/2) == t1:
			c1 += countleft
		elif int(left/2) == t2:
			c2 += countleft
		if left - int(left/2) - 1 == t1:
			c1 += countleft
		elif left - int(left/2) - 1 == t2:
			c2 += countleft
		if int(right/2) == t1:
			c1 += countright
		elif int(right/2) == t2:
			c2 += countright
		if right - int(right/2) - 1 == t1:
			c1 += countright
		elif right - int(right/2) - 1 == t2:
			c2 += countright
		left = t1
		right = t2
		countleft = c1
		countright = c2

	if k - countk < countleft:
		if countk + int((countleft-countright)/2) > k:
			print("Case #",i+1,": ",left," ",left,sep='')
		else:
			print("Case #",i+1,": ",left," ",right,sep='')
	else:
		print("Case #",i+1,": ",right," ",right,sep='')
