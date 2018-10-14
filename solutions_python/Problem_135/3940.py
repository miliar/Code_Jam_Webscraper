
def findnum(one,two):
	count = 0
	for i in range(0,4):
		if one[i] in two :
			count += 1
			flag = one[i]
	if count==1:
		return str(flag)
	if count==0:
		return 'Volunteer cheated!'
	if count>1:
		return 'Bad magician!'	

while True:
	f = open('A-small-attempt3.in','r');
	case = f.readline()
	case_num = 1
	while True:
		FirstQ = int(f.readline())
		FirstRow1 = f.readline().split()
		SecondRow1 = f.readline().split()
		ThirdRow1 = f.readline().split()
		FourthRow1 = f.readline().split()
		First = [FirstRow1,SecondRow1,ThirdRow1,FourthRow1]
		SecondQ = int(f.readline())
		FirstRow2 = f.readline().split()
		SecondRow2 = f.readline().split()
		ThirdRow2 = f.readline().split()
		FourthRow2 = f.readline().split()
		Second = [FirstRow2,SecondRow2,ThirdRow2,FourthRow2]
		message = findnum(First[FirstQ-1],Second[SecondQ-1])
		print 'Case #' + str(case_num) + ': ' + message
		case_num += 1



