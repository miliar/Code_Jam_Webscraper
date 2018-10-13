file = open("newfile.txt", "w")
file1 = open("A-small-attempt0.in.txt","r")
data = file1.readlines()
T=int(data[0])
for i in range (1,T+1):
	k=(i*10)-9
	data1=data[k].split()
	data2=data[k+int(data1[0])].split()
	data1=data[k+5].split()
	data3=data[k+5+int(data1[0])].split()
	flag=0
	numb=0
	for da in data2:
		for da1 in data3:
			if da==da1:
				flag+=1
				numb=int(da)
	if flag==0:
		file.write("Case #%d: Volunteer cheated!\n"% (i))
	if flag==1:
		file.write("Case #%d: %d\n"% (i,numb))
	if flag>1:
		file.write("Case #%d: Bad magician!\n"% (i))
	
	
file1.close()
file.close()
