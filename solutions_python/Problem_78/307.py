import sys
filename = sys.argv[1]
file = open(filename, 'r')
cases = int(file.readline())
for n in range(1, cases+1):
	data = file.readline().strip('\n').split(' ')
	maxToday = int(data[0])
	pToday = int(data[1])/100.0
	pTotal = int(data[2])/100.0
	today = False
	total = False
	tToday = 0
	todayLost = 0
	if(int(data[1]) != 0 and int(data[2]) == 0):
		print "Case #{}: Broken".format(n)
	elif(int(data[1]) != 1 and int(data[2]) == 1):
		print "Case #{}: Broken".format(n)
	else:
		for i in range(maxToday):
			win = (pToday*(maxToday-i))
			loses = (maxToday-i) - win
			if(abs(win - round(win)) <= 0.00001):
				today = True
				tToday = maxToday-i
				todayLost = loses
				break
		if today:
			for i in range(tToday, 100+1):
				win = (pTotal*i)
				loses = i - win
				if((abs((pTotal*i) - round((pTotal*i))) <= 0.00001) and (loses >= todayLost)):
					total = True
					break
		if(today and total):
			print "Case #{}: Possible".format(n)
		else:
			print "Case #{}: Broken".format(n)