INPUT_FILE = r'C:\Downloads\FromFirefox\A-large(1).in'
OUTPUT_FILE = r'C:\Users\Assaf\Fun\codeJam\large.out'

inputFile = file(INPUT_FILE, 'rb')
numQuestions = int(inputFile.readline())
outputFile = file(OUTPUT_FILE, 'wb')

def solveQuestion(table, numTeams):
    gamesPlayed = []
    for row in table:
        gamesPlayed.append(row.count('1') + row.count('0'))
    allWps = []
    for i, row in enumerate(table):
        wins = row.count('1')
        allWps.append(float(wins) / gamesPlayed[i])
    allWpsPlusOne = []
    allWpsMinusOne = []
    for i, row in enumerate(table):
        wins = row.count('1')
        allWpsPlusOne.append(float(wins) / (gamesPlayed[i] - 1))
        allWpsMinusOne.append(float(wins - 1) / (gamesPlayed[i] - 1))
    allOwps = []
    for i in xrange(numTeams):
        owp = 0.0
        count = 0
        for t in xrange(numTeams):
            if t == i:
                continue
            if '1' == table[t][i]:
                owp += allWpsMinusOne[t]
                count += 1
            elif '0' == table[t][i]:
                owp += allWpsPlusOne[t]
                count += 1
            elif '.' == table[t][i]:
                continue
            else:
                raise Exception("Table error")
        allOwps.append(float(owp) / (count))
    allOowps = []
    for i in xrange(numTeams):
        oowp = 0.0
        for t in xrange(numTeams):
            if '.' != table[i][t]:
                oowp += allOwps[t]
        allOowps.append( oowp / gamesPlayed[i] )
    for i in xrange(numTeams):
        rpi = \
                (0.25 * allWps[i]) + \
                (0.50 * allOwps[i]) + \
                (0.25 * allOowps[i])
        outputFile.write('%.12g\n' % rpi)

for q in xrange(numQuestions):
    outputFile.write("Case #%d:\n" % (q+1))
    numberOfTeams = int(inputFile.readline())
    table = []
    for team in xrange(numberOfTeams):
        row = list(inputFile.readline()[:numberOfTeams])
        table.append(row)
    result = solveQuestion(table, numberOfTeams)

outputFile.close()
inputFile.close()
# print file(OUTPUT_FILE, 'rb').read()

