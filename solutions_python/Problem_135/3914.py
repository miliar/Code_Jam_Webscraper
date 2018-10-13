def examineLists(list1, list2):
	elements_both = set(list1) & set(list2)
	el =  len(elements_both)
	if(el ==1):
		for i in list1:
			if i in list2:
				return i
	else:
		if(el==0):
			return "Volunteer cheated!"
		else:
			return "Bad magician!"


file = open('A-small-attempt0.in','r')
row = []
guessed_row = []
output = []
allrows = []
#tc_input = raw_input()
tc_input = file.readline()
tC = int(tc_input)
if (not(tC>=1 and tC <=100 )):
	exit()
for i in range(tC):
	output.append("Case #" + str(i+1) + ": ")
	del row[:]
	del guessed_row[:]
	for j in range(2):
#		rowNumber_inp = raw_input()
		rowNumber_inp	= file.readline()
		rowNumber = int(rowNumber_inp)
		if (not(rowNumber>=1 and rowNumber <=4 )):
			exit()
		del row[:]
		del allrows[:]
		#row.append(raw_input())
	  #row.append(raw_input())
		#row.append(raw_input())
		#row.append(raw_input())
		row.append(file.readline())
		row.append(file.readline())
		row.append(file.readline())
		row.append(file.readline())
		guessed_row.append(row[rowNumber-1])
	
	list1 = guessed_row[0].split()
	list2	= guessed_row[1].split()
	output.append(examineLists(list1,list2))

file.close()
theRange = len(output)
itr = 0
theOutput = ""
while(itr < theRange-1):
#	print output[itr] + output[itr+1]
	theOutput += output[itr] + output[itr+1] + "\n"
	itr+=2

file = open("outputfile.txt","w")
file.write(theOutput)
file.close()	
