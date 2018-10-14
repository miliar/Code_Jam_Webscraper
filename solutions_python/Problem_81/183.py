testName = 'A'
#testName = 'A-small-practice'
testName = 'A-small-attempt0'
testName = 'A-large'
#testName = 'A-test'

inputFile = open(testName+'.in', 'r')
input = inputFile.read()
inputFile.close()
del inputFile

output = ""

lines = input.split("\n")
pop = lines.pop
del input

def getWinPerc(teamGames, excludeTeam = -1):
	won = 0
	playAgaiExclude = 0
	for i in teamGames:
		if i == excludeTeam:
			playAgaiExclude = 1
		elif teamGames[i] == '1':
			won += 1
	return float(won) / (len(teamGames) - playAgaiExclude)

def getOpWinPerc(teamGames, teams, excludeTeam = -1):
	tot = 0.0
	for i in teamGames:
		tot += getWinPerc(teams[i], excludeTeam)
	return tot / len(teamGames)

T = int( pop(0) )

for test in range(T):
	N = int(pop(0))
	Nrange = range(N)
	teams = [{} for i in range(N)]

	for i in Nrange:
		curTeam = teams[i]
		r = pop(0)
		for j in Nrange:
			s = r[j]
			if s != '.': curTeam[j] = s

	output += "Case #%d: \n" % (test + 1)

	for t in Nrange:
		curTeam = teams[t]
		WP = getWinPerc(curTeam)
		OWP = getOpWinPerc(curTeam, teams, t)
		tot = 0.0
		for i in curTeam:
			tot += getOpWinPerc(teams[i], teams, i)
		

		print test, t

		OOWP = tot / len(curTeam)
		output += str(0.25 * WP + 0.5*OWP + 0.25 * OOWP) + "\n"

	print test

print output

outputFile = open(testName+'.out', 'w')
outputFile.write(output)
outputFile.close()
