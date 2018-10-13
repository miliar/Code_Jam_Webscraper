
table = {3: [1, 2],2: [1, 1],4: [2, 2],5: [2, 3],7: [3, 4],6: [3, 3],8: [4, 4],9: [4, 5],1: [0, 1],}
num_cases = int(input())
count = 1
while (num_cases):
	x = int(input())
	q = list(input().split())
	q = [int(i) for i in q]
	r = [int(i) for i in q]					# defining a list.
	array1 = [float("inf")]
	it = 0
	if q.count(9) is 1:
		while any(i>1 for i in q):
			maxval = max(q)                                      
			array1.append(maxval+ it)
			it += 1
			if maxval is 9:
				q.append(3)
				q.append(6)
			else:
				q.append(table[maxval][0])
				q.append(table[maxval][1])
			i = q.index(maxval)
			del(q[i])
	q = r
	array2 = [float("inf")]
	it = 0
	if any(i>1 for i in q):
		while any(i>1 for i in q):
			maxval = max(q)							# finding the maximum value.
			array2.append(maxval+ it)
			it += 1
			q.append(table[maxval][0])
			q.append(table[maxval][1])
			i = q.index(maxval)
			del(q[i])								# deleting this element.
		print("Case #"+ str(count) + ": " + str(min(min(array2), min(array1))))
	else:		
		print("Case #"+ str(count) + ": 1")
	num_cases =  num_cases-1
	count = count+1