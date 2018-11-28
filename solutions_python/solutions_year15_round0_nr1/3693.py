fo = open('A-small-attempt1.in', 'r')

count = 0
summ = 0
index = 1
next(fo)
for line in fo:
	for i in range(2, len(line)-1):
		l = int(i)-2
		t = int(line[i])
		if i == 2:
			summ = t
		else:
			if summ+count < l and t != 0:
				count = l-summ+count
				summ = l-summ+count+t
				#print('true')
				#print(summ, count, l)
			else:
				summ = summ + t
				#print('false')
				#print(summ, count, l)
		
	print('Case #' + str(index) + ': ' + str(count))
	count = 0
	summ = 0
	index +=1

fo.close()