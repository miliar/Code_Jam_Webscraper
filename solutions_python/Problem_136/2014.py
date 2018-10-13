t = int(input())
for i in range (1, t+1):
	totalrate = 2.0
	line = input().split()
	c = float(line[0]) # price of farm
	f = float(line[1]) # production output of farm
	x = float(line[2]) # target cookie goal
	totalcookies = 0.0
	time = 0.0
	while totalcookies != x:
		remainingtime = x / totalrate
		maybetime = (x) / (totalrate+f) + c/totalrate
		if remainingtime > maybetime:
			time += c/totalrate
			totalrate += f
		else:
			time += x/totalrate
			break
	print('Case #{0}: {1:.9f}'.format(i, time))
