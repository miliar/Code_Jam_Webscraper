import sys

input = open(sys.argv[1], 'r')
output = open(sys.argv[2], 'w')

cases = input.readline()
cases = int(cases)

for x in range(cases):
	
	numteams = int(input.readline())
	teams = []
	tplayed = []
	record = []
	
	for y in range(numteams):
		w = 0.0
		g = 0.0
		t = input.readline()
		record.append(t)
		for z in t:
			if z == '1':
				w += 1.0
				g += 1.0
			elif z == '0':
				g += 1.0
		teams.append([w, g, w/g])
	for y in record:
		ipl = []
		for z in range(numteams):
			if y[z] != '.':
				ipl.append(z)
		tplayed.append(ipl)
		
	for y in range(numteams):
		otot = 0.0
		tw = 0.0
		tg  = 0.0
		for z in tplayed[y]:
			tw = teams[z][0] - float(record[z][y])
			tg = teams[z][1] - 1
			otot += tw/tg
		teams[y].append(otot/len(tplayed[y]))
		
	for y in range(numteams):
		ootot = 0.0
		for z in tplayed[y]:
			
			ootot += teams[z][3]
		teams[y].append(ootot/(len(tplayed[y])))
	
	output.write("Case #%i:\n" %(x+1))
	for y in teams:
		output.write("%.8f\n" % (0.25*y[2] + 0.5*y[3] + 0.25*y[4]))


input.close()
output.close()


