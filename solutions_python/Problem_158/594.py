file_write=open("ominos_output.txt","w+")
file_read=open("D-small-attempt2.in","r")
noOfTestCases=int(file_read.readline())
for i in range(1,noOfTestCases+1):
	x,row,column = file_read.readline().split()
	x=int(x)
	row = int(row)
	column = int(column)
	if(column<row):
		row,column=column,row
	if(x==1):
		file_write.write("Case #%d: GABRIEL\n"%(i))
	if(x==2):
		total = row*column
		if((total%2)==0):
			file_write.write("Case #%d: GABRIEL\n"%(i))
		else:
			file_write.write("Case #%d: RICHARD\n"%(i))
	if(x==3):
		total=row*column
		if((total%3)!=0):
			file_write.write("Case #%d: RICHARD\n"%(i))
		else:
			if(row==1):
				file_write.write("Case #%d: RICHARD\n"%(i))
			else:
				file_write.write("Case #%d: GABRIEL\n"%(i))
	if(x==4):
		total=row*column
		if((total%4)!=0):
			file_write.write("Case #%d: RICHARD\n"%(i))
		else:
			if(row==2):
				file_write.write("Case #%d: RICHARD\n"%(i))
			elif(row==1):
				file_write.write("Case #%d: RICHARD\n"%(i))
			elif(row==3):
				file_write.write("Case #%d: GABRIEL\n"%(i))
			elif(row==4):
				file_write.write("Case #%d: GABRIEL\n"%(i))

