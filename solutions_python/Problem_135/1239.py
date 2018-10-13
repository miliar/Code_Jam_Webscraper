f=file("A-small-attempt1.in")
op=file("A.op","w")
total_line=f.readline()
total_line=int(total_line)

for i in range(total_line):
	ans_1=int(f.readline())
	for j in range(4):
		cards=f.readline()
			
		if j==ans_1-1:
			card_list=cards.split(' ')
			card_list[-1]=card_list[-1].split('\n')[0]
			list1= card_list
	
	ans_2=int(f.readline())
	
	
	for j in range(4):
		cards=f.readline()
			
		if j==ans_2-1:
			card_list=cards.split(' ')
			card_list[-1]=card_list[-1].split('\n')[0]
			list2= card_list

	result=[]
	for data1 in list1:
		for data2 in list2:
			if data1== data2:
				result.append(data1)
				
	string = "case #"+str(i+1)+": "
	if len(result)==1:
		string= string + str(result[0])
		
	elif len(result)==0:
		string = string+"Volunteer cheated!" 	

		
	else:
		string = string+"Bad magician!"
	print string
	op.write(string+"\n")
