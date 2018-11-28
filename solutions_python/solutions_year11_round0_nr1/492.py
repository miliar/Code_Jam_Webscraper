
def bottrust(data):
	commands = data.split(' ')
	opos = 1
	otime = 0
	bpos = 1
	btime = 0
	for i in range(1,len(commands),2):
		if commands[i] == 'O':
			tt = abs(int(commands[i+1]) - opos) + 1
			otime += tt
			opos = int(commands[i+1])
			if otime <= btime:
				otime = btime + 1
			#print "push button " + commands[i+1] + " at " + str(otime)
		if commands[i] == 'B':
			tt = abs(int(commands[i+1]) - bpos) + 1
			btime += tt
			bpos = int(commands[i+1])
			if btime <= otime:
				btime = otime + 1
			#print "push button " + commands[i+1] + " at " + str(btime)
	return max(otime,btime)
	
def solveBotTrust():
	f = open('gcjdata.txt','r')
	lines = f.readlines()
	for i in range(1,len(lines)):
		print "Case #{0}: {1}".format(i,bottrust(lines[i]))
		
solveBotTrust()