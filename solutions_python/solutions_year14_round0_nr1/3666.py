from __future__ import print_function

def gridCheck(pre, post):
	ret = []
	for i in range(0, len(pre)):
		if pre[i] in post:
			ret.append(pre[i])
	return ret
	
			
fileOfInt = 'A-small.in'
fileOut = 'A-small.out'
fOut = open(fileOut,'w')
games = []
with open(fileOfInt) as f:
	i = 0
	for line in f:
		if i == 0:
			totalCount = int(line)
			i = i + 1
			continue
		i = i + 1
		games.append(line.strip().split())
		
for i in range(0, totalCount):
	output = "Case #"+str(i+1)+": "
	preRow = int(games[i*10][0])
	preGrid = games[i*10+1:i*10+5]
	postRow = int(games[i*10+5][0])
	postGrid = games[i*10+6:i*10+10]
	result = gridCheck(preGrid[preRow-1], postGrid[postRow-1])
	if len(result) == 1:
		output = output + result[0]
	elif len(result) > 1:
		output = output + "Bad magician!"
	else:
		output = output + "Volunteer cheated!"
	#print output
	print(output, file=fOut)	
fOut.close()
#print games


