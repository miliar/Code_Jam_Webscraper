import sys

file = open('input.txt', 'r')
testcase=int(file.readline())
#print testcase
case=1
while case <=testcase:
	firstrow=int(file.readline())
	#print firstrow
	i=1
	while i<=4:
		firstrowline=file.readline()
		if i==firstrow:
			
			firstrowline=firstrowline.strip()
			firstlist=map(int, firstrowline.split(' '))
		i=i+1
	secondrow=int(file.readline())
	#print secondrow
	i=1
	while i<=4:
		secondrowline=file.readline()
		if i==secondrow:
			
			secondrowline=secondrowline.strip()
			seclist=map(int, secondrowline.split())
		i=i+1
	count =0
	matchele=""
	for ele in  seclist:
		if ele  in firstlist :
			count =count+1
			matchele=str(ele)
	resultstr="Case #"+str(case)+":" 
	if count==0:
		print resultstr+ " "+"Volunteer cheated!"
	elif count ==1:
		print resultstr+ " "+matchele	
	elif count >1:
		print resultstr+ " "+"Bad magician!"
	case =case+1

