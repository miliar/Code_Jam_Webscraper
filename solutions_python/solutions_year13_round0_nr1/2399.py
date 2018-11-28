

results = []




inputFile = open('A-large.in','r')
input = inputFile.read()

lines = input.split('\n')
numGames = lines.pop(0)
games = []
for x in xrange(0,len(lines),5):
	games.append(lines[x:x+4])
	
games.pop(len(games) -1)


for g in xrange(0,int(numGames),1):



	for l in xrange(0,len(games[g]),1):
		
		temp = []
		for c in xrange(0,4,1):

			temp.append(games[g][l][c])

		games[g][l] = temp
count = 1
for game in games:
	draw = False
	result = False
	#check horizontal
	if result == False:
		for l in game:

			line = []
			for c in l:
				line.append(c)
			line.sort()
			if (line[0] == line[3] or (line[0]==line[2] and line[3] == 'T') or (line[1] ==line[3] and line[0] == 'T')) and line[0] != '.':
				result = True
				results.append(line[2] + ' won')
				print line[2] , ' won horizontal'
				
			elif line[0] == '.':
				draw = True
	#check vertical
	if result == False:
		for x in xrange(0,4,1):
			line = []
			for y in xrange(0,4,1):
				line.append(game[y][x])
			line.sort()
			if (line[0] == line[3] or (line[0]==line[2] and line[3] == 'T') or (line[1] ==line[3] and line[0] == 'T')) and line[0] != '.':
				result = True
				results.append(line[2] + ' won')
				print line[2] , ' won vertical'
				
			elif line[0] == '.':
				draw = True
	#check diagonal
	#1,1 2,2 3,3 4,4
	#1,4 2,3 3,2 1,1
	if result == False:
		line = [game[0][0],game[1][1],game[2][2],game[3][3]]
		line.sort()
		if (line[0] == line[3] or (line[0]==line[2] and line[3] == 'T') or (line[1] ==line[3] and line[0] == 'T')) and line[0] != '.':
			result = True
			results.append(line[2] + ' won')
			print line[2] , ' won diagnoal1'
			
		elif line[0] == '.':
			draw = True
			
	if result == False:
		line = [game[0][3],game[1][2],game[2][1],game[3][0]]
		line.sort()
		if (line[0] == line[3] or (line[0]==line[2] and line[3] == 'T') or (line[1] ==line[3] and line[0] == 'T')) and line[0] != '.':
			result = True
			results.append(line[2] + ' won')
			print line[2] , ' won diagnoal2'

		
		elif line[0] == '.':
			draw = True	
#check draw
	if result == False and draw == True:
		results.append('Game has not completed')
		print 'not completed'
	elif result == False:
		results.append('Draw')
		print 'draw'
	count += 1
		

	

f = open('output.txt', 'r+')




for g in xrange(0,int(numGames),1):
	print '\nGAME\n'
	for l in games[g]:
		print l
	print '\n'
	writestring = 'Case #' + str(g+1) + ': ' + results[g] + '\n'
	print writestring
	f.write(writestring)
	#check vertical
print results
	#check diagonal
	

#case 1: x win
#case 2: 0 win
#case 3: draw = no win and a dot

#check for 