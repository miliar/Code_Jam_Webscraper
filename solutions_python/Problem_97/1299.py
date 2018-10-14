def solve(case):
	case = [int(i) for i in case.split()]
	min = case[0]
	max = case[1]
	count = 0

	for i in range(min,max+1):
		num = str(i)
		ls = []
		for j in range(len(num)-1):
			num = num[-1] + num[:-1]
			numt = int(num)
			if numt>=min and numt<=max and numt>i and str(num) not in ls: 
				count+=1
			ls.append(num)
			num = str(num)
		
	return str(int(count))
			
file = open('C-large.in','r')
lines = file.readlines()
file.close()

linesout = []
toout = ''
for i in range(1,len(lines)):
	toout = solve(lines[i])
	print(i)
	linesout.append('Case #' + str(len(linesout) + 1) + ': ' + toout + '\n')
	toout = ''

linesout[-1] = linesout[-1][:-1]
file = open('out','w')
file.writelines(linesout)