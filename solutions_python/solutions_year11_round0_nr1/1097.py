if __name__ == '__main__':
	fin = open("A-large.in", 'r')
	fout = open("out.txt", 'w')
	numCases = int(fin.readline())
	for item in range(numCases):
		inpLine = fin.readline().split()
		numAction = int(inpLine[0])
		i = 1
		info = {'O' : {'time' : 0, 'position': 1}, 'B': {'time' : 0, 'position': 1}}
		totalTime = 0
		for action in range(numAction):
			robo = inpLine[i]
			pos = int(inpLine[i+1])
			timeReq = info[robo]['position'] - pos
			if timeReq < 0:
				timeReq *= -1
			if (info[robo]['time'] + timeReq) > totalTime:
				totalTime += (info[robo]['time'] + timeReq - totalTime)
			totalTime += 1
			info[robo]['time'] = totalTime
			info[robo]['position'] = pos
			i += 2
		#print 'Case #%d: %d'%(item+1, totalTime)
		fout.write('Case #%d: %d\n'%(item+1, totalTime))
