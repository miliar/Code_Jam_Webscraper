#Standing ovation
fin = open('A-large.in','r')
fout = open('out.large','w+')

totalCases = int(fin.readline())
for i in range(totalCases):
	case = fin.readline().split(' ')
	sMax = int(case[0])
	friend = 0
	totalPeople = 0
	for j in range(sMax+1):
		if totalPeople >= j:
			totalPeople += int(case[1][j])
		else:
			friend += j - totalPeople
			totalPeople = j + int(case[1][j])
	fout.writelines('Case #%d: %d\n' % (i+1,friend))

fout.close()
fin.close()