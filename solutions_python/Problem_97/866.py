
def func(arr, num):
	min = int(arr[0])
	max = int(arr[1])
	
	retval = 0
	count = min
	arr = []
	while count <= max:
		if count in arr:
			count+=1
			continue
		temparr = []
		temparr.append(count)
		for i in range(len(str(count))):
			reorg = str(count)[-(i+1):] + str(count)[:-(i+1)]

			if int(reorg)!=count and int(reorg) <= max and int(reorg) >= min and int(reorg) not in temparr:
				if count not in arr:
					arr.append(count)
				arr.append(int(reorg))
				temparr.append(int(reorg))

		if len(temparr) > 1:
			retval+=(len(temparr) * (len(temparr) - 1) / 2)

		count+=1

	
	print "Case #" + str(num+1) + ": " + str(retval)

T = raw_input()
inp = []
for i in range(int(T)):
	inp.append(raw_input())
	
for j in range(len(inp)):
	arr = inp[j].split()
	func(arr, j)
