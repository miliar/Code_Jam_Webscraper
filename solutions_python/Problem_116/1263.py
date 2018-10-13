def CheckWiner(arr2,ch):
	temparr=list(arr2)
	for i in range(len(temparr)):
		temparr[i]=temparr[i].replace('T',ch)
	key=ch*4
	if key in temparr:
		return True
	

def CheckDraw(arr2):
	temparr=list(arr2)
	ch=set('.')
	for word in temparr:
		if ch & set(word):
			return True
	return False	

file1 = open("sample3.txt","r")
file2 =open("output1.txt","w")
testcount=int(file1.readline())
for caseno in range(1,testcount+1):
	count=0
	arr = []
	for i in range(4):
		nkstr=file1.readline()
		arr.append(nkstr)
	nkstr=file1.readline()
	#print arr
	arr2=list(arr)
	for i in  range(len(arr2)):
		arr2[i]= arr2[i].rstrip()
	for  i in range (4):
		ch=arr[0][i]+arr[1][i]+arr[2][i]+arr[3][i]
		arr2.append(ch);
	
	ch=""
	
	for  i in range (4):
		ch=ch+arr[i][i]
	arr2.append(ch)

	
	ch=""
	ch= arr[0][3]+arr[1][2]+arr[2][1]+arr[3][0]
	arr2.append(ch)
	#print arr2
	#print 
	
	winner=CheckWiner(arr2,"X")
	if winner:
		printstr= "Case #"+str(caseno)+":"+" " +"X won"+"\n"
	else:
		winner=CheckWiner(arr2,"O")
		if winner:
			printstr= "Case #"+str(caseno)+":"+" " +"O won"+"\n"
		else:
			draw=CheckDraw(arr2)
			if draw:
				printstr= "Case #"+str(caseno)+":"+" " +"Game has not completed"+"\n"
				
			else:
				printstr= "Case #"+str(caseno)+":"+" " +"Draw"+"\n"
	#print printstr
	
	file2.write(printstr)

file1.close()
file2.close()

