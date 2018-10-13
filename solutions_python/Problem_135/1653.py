input_file = open('input.txt')

n = int(input_file.next())

for i in range(1,n+1):
	guess1 = int(input_file.next())
	for j in range(1,5):
		if j == guess1:
			arr1 = map(int,input_file.next().split(' '))
		else:
			input_file.next()
	guess2 = int(input_file.next())
	for j in range(1,5):
		if j == guess2:
			arr2 = map(int,input_file.next().split(' '))
		else:
			input_file.next()
	
	print 'Case #%s:' % i,
	
	ans = list(set(arr1) & set(arr2))
	if len(ans) == 1: print ans[0]
	elif len(ans) == 0: print 'Volunteer cheated!'
	else: print 'Bad magician!'
		