f = open('input.txt', 'r')
outfile = open('output.txt', 'w')

numcases = f.readline()
numcases = int(numcases)

def diff(a, b):
	if(a>b):
		return a-b
	elif(b>a):
		return b-a
	return 0

for case in range(numcases):
	thisline = f.readline().split()
	index = 0
	pushes = thisline[index]
	index+=1
	pushes = int(pushes)
	time = 0
	posits = [1, 1]
	last_time_moved = [0, 0]
	for push in range(pushes):
		bot = thisline[index]
		index += 1
		if(bot=="O"):
			bot = 0
		else:
			bot = 1
		if push==0:
			curbot = bot
		butt = thisline[index]
		index += 1
		butt = int(butt)
		if(bot==curbot):
			time+=diff(butt, posits[bot])+1
			posits[bot]=butt
			last_time_moved[bot]=time
		else:
			curbot=bot
			timeneeded = diff(posits[bot], butt)+1
			timesincelastmove = time - last_time_moved[bot]
			if timeneeded <= time-last_time_moved[bot]:
				time+=1
				last_time_moved[bot]=time
			else:
				time += timeneeded - timesincelastmove
				last_time_moved[bot]=time
			posits[bot] = butt
	outfile.write('Case #' + str(case+1) +': '+str(time)+'\n')
		
			