test = int(raw_input())
inte = 1
while(test):
	
	finallist1 = []
	finallist2 = []
	count = 0
	question1 = int(raw_input())
	for i in range(4):
		list = raw_input()
		list = list.split()
		finallist1 = finallist1 + list
	
	question2  = int(raw_input())
	for i in range(4):
		list = raw_input()
		list = list.split()
		finallist2 = finallist2 +list
	
	test = test -1	
	index1= (question1-1)*4
	
	index2 = (question2-1)*4
	
	list1= finallist1[index1 : index1+4]
	list2 = finallist2[index2: index2+ 4]
	result = []
	for element in list1:
		if element in list2:
			result.append(element)

	for item in result:
		count = count +1
	if count == 1:
		print 'Case #%d: %s' % (inte, result[0])
	elif count == 0:	
		print 'Case #%d: %s' % (inte,'Volunteer cheated!')
	else:
		print 'Case #%d: %s' % (inte,'Bad magician!')
	inte = inte + 1
	