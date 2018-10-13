#OminousOmino
fin = open('D-small-attempt1.in','r')
fout = open('small.out','w+')

def print_case(caseNum,winner):
	win=''
	if winner == 'r':
		win = 'RICHARD'
	else:
		win = 'GABRIEL'
	fout.write('Case #%d: %s\n' % (caseNum+1,win))

totalCases = int(fin.readline())
for i in range(totalCases):
	case = fin.readline().split(' ')
	x = int(case[0])
	r = int(case[1])
	c = int(case[2])
	if x == 1:
		print_case(i,'g')
	elif x==2:
		if (r*c)>=2 and (r*c)%2==0:
			print_case(i,'g')
		else:
			print_case(i,'r')
	elif x==3:
		if r==1 or c==1:
			print_case(i,'r')
		elif (r*c)>=3 and (r*c)%3==0:
			print_case(i,'g')
		else:
			print_case(i,'r')
	elif x==4:
		if r==1 or c==1:
			print_case(i,'r')
		elif r==2 or c==2:
			print_case(i,'r')
		elif (r*c)<4:
			print_case(i,'r')
		elif (r*c)%4!=0:
			print_case(i,'r')
		else:
			print_case(i,'g')
			
fout.close()
fin.close()