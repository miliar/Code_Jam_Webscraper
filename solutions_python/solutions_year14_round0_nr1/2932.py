ans = []
num_of_testcases = int(raw_input())
for i in range(0,num_of_testcases):
	num_row_1 = int(raw_input())
	row1 = [[] for i in range(0,4)]
	for k in range(0,4):
		temp = raw_input()
		row1[k] = map(int,temp.split())
		#print 'row 1 is {0}'.format(row1[k])
	num_row_2 = int(raw_input())
	row2 = [[] for i in range(0,4)]
	for k in range(0,4):
		temp = raw_input()
		row2[k] = map(int,temp.split())
		#print 'row 2 is {0}'.format(row2[k])
	chk_list = set(row1[num_row_1 -1 ]) & set(row2[num_row_2 -1 ])
	#print len(chk_list)
	if len(chk_list) > 1:
			ans.append("Bad magician!")
	elif  len(chk_list) == 1 :
		for j in row1[num_row_1-1]:
			if j in row2[num_row_2-1]:
				ans.append(str(j))
	else :
		ans.append("Volunteer cheated!")

num = 1
for i in ans :
	print "Case #{0}: {1}".format(num,i)
	num += 1