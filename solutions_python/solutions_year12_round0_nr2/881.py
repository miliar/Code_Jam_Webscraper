def func(arr, num):
	n = int(arr[0])
	s = int(arr[1])
	p = int(arr[2])
	arr2 = arr[3:]
	
	if p==0:
		print "Case #" + str(num+1) + ": " + str(len(arr2))
		return
	
	retarr = 0
	check = []
	
	for i in arr2:
		if int(i)==0:
			x=5
		elif p*3 <= int(i)+2:
			retarr+=1
		else:
			check.append(i)
			
	for j in check:
		if s <= 0:
			break
			
		if p*3 <= int(j)+4:
			s-=1
			retarr+=1
	
	print "Case #" + str(num+1) + ": " + str(retarr)

T = raw_input()
inp = []
for i in range(int(T)):
	inp.append(raw_input())
	
for j in range(len(inp)):
	arr = inp[j].split()
	func(arr, j)

