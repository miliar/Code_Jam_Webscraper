
table = {3: [1, 2],2: [1, 1],4: [2, 2],5: [2, 3],7: [3, 4],6: [3, 3],8: [4, 4],9: [4, 5],1: [0, 1],}
test = int(input())
count = 1
while (test):
	x = int(input())
	li = list(input().split())
	li = [int(i) for i in li]
	list2 = [int(i) for i in li]
	array = [float("inf")]
	inx = 0
	if li.count(9) is 1:
		while any(i>1 for i in li):
			maximum = max(li)
			array.append(maximum+ inx)
			inx += 1
			if maximum is 9:
				li.append(3)
				li.append(6)
			else:
				li.append(table[maximum][0])
				li.append(table[maximum][1])
			i = li.index(maximum)
			del(li[i])
	li = list2
	arr = [float("inf")]
	inx = 0
	if any(i>1 for i in li):
		while any(i>1 for i in li):
			maximum = max(li)
			arr.append(maximum+ inx)
			inx += 1
			li.append(table[maximum][0])
			li.append(table[maximum][1])
			i = li.index(maximum)
			del(li[i])
		print("Case #"+ str(count) + ": " + str(min(min(arr), min(array))))
	else:		
		print("Case #"+ str(count) + ": 1")
	test =  test-1
	count = count+1