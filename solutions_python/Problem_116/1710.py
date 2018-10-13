
pas = raw_input()
for i in range(int(pas)):
	arr = []
	result = -1
	isDot = False
	#Rows
	for a in range(4):
		vas = raw_input()
		if len([1 for v in vas if v == '.']) > 0:
			isDot = True
			
		if (len([1 for v in vas if v == 'X']) + len([1 for v in vas if v == 'T'])) == 4:
			result = 'X won'
		elif (len([1 for v in vas if v == 'O']) + len([1 for v in vas if v == 'T'])) == 4:
			result = 'O won'
			
		arr.append(vas)
	
	if (i+1 != int(pas)):
		raw_input()
	
	#Columns
	if result == -1:
		for b in range(4):
			ves = [row[b] for row in arr]
			if (len([1 for v in ves if v == 'X']) + len([1 for v in ves if v == 'T'])) == 4:
				result = 'X won'
				break
			elif (len([1 for v in ves if v == 'O']) + len([1 for v in ves if v == 'T'])) == 4:
				result = 'O won'
				break
				
	#Diagional
	if result == -1:
		x1 = arr[0][0]+arr[1][1]+arr[2][2]+arr[3][3]
		x2 = arr[0][3]+arr[1][2]+arr[2][1]+arr[3][0]
		if (len([1 for v in x1 if v == 'X']) + len([1 for v in x1 if v == 'T'])) == 4:
			result = 'X won'
		elif (len([1 for v in x1 if v == 'O']) + len([1 for v in x1 if v == 'T'])) == 4:
			result = 'O won'
		if (len([1 for v in x2 if v == 'X']) + len([1 for v in x2 if v == 'T'])) == 4:
			result = 'X won'
		elif (len([1 for v in x2 if v == 'O']) + len([1 for v in x2 if v == 'T'])) == 4:
			result = 'O won'
	
	if result == -1 and isDot:
		result = 'Game has not completed'
	elif result == -1 and not isDot:
		result = 'Draw'

	print 'Case #' + str(i+1) + ': ' + str(result)