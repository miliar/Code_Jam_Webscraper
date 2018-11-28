kase = 1
ans = 0
t = int(input())
while kase <= t:
	inp = input().split(' ')
	lower = int(inp[0])
	upper = int(inp[1])
	low = lower
	while low<= upper:
		curr = str(low)
		count = 0
		list = []
		if low < 10 :
			low = low + 1
			list
			continue
		n = len(curr)
		#print (curr,"---->")
		for i in range(1,n):
			temp = curr[i:] + curr[:i]
			list.append(curr)
			#print (temp)
			if (int(temp) > int(curr) and int(temp) >= lower and int(temp) <= upper and list.count(temp)==0):# and len(str(int(temp))) == len(curr) ) :
				count = count + 1
				list.append(temp)
		#print (list)
		#print (curr,"count", count)
		ans = ans + count
		lis = []
		low = low + 1
	outstr = "Case #" + str(kase) + ": " + str(ans)
	print (outstr)
	kase = kase + 1
	ans = 0