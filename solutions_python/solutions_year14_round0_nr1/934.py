n = int(raw_input())
for i in range(0,n):

	ren_1 = int(raw_input())
	data_1 = ""
	for j in range(0,4):
		if( j == (ren_1 -1)):
			data_1 = raw_input()
		else:
			raw_input()
	data_1 = data_1.split()

	ren_2 = int(raw_input())
	data_2 = ""
	for j in range(0,4):
		if( j == (ren_2 -1)):
			data_2 = raw_input()
		else:
			raw_input()
	data_2 = data_2.split()

	common = list(set(data_1) & set(data_2))

	if(len(common) == 1):
		print 'Case #' + str(i+1) + ': ' + common[0]
	elif(len(common) > 1):
		print 'Case #' + str(i+1) + ': ' + 'Bad magician!'
	elif(len(common) == 0):
		print 'Case #' + str(i+1) + ': ' + 'Volunteer cheated!'