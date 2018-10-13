import sys

sinfile = sys.argv[1]
soutfile = sinfile[:-2] + 'out'

finfile = open(sinfile)
foutfile = open(soutfile, 'w')

n = int(finfile.readline().strip())

for i in range(1, n+1):
	oneline = finfile.readline().strip().split(' ')
	steps = int(oneline[0])
	
	lastrobot = None
	toind = {'O':0, 'B': 1}
	lastspent = [0, 0]
	lastpos = [1, 1]
	#otherstime = 0
	#otherstime = 0
	for j in range(steps):
		robot = toind[oneline[j*2+1]]
		button = int(oneline[j*2+2])

		selftime = abs(button  - lastpos[robot]) + 1
		lastpos[robot] = button
		
		lastspent[robot] += selftime

		if lastrobot is None:
			lastrobot = robot
			
		
		if lastrobot != robot:
			if lastspent[robot] <= lastspent[not robot]:
				# wait until other press
				lastspent[robot] = lastspent[not robot] + 1
			lastrobot = robot
	
	ans = max(lastspent)

	print >> foutfile, 'Case #%d: %s' % (i, ans)
