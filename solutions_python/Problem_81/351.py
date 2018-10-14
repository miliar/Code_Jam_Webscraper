from string import rstrip
import sys

def calcWp(result):
    wins = 0
    gp   = 0
    for char in result:
        if char == '1':
            wins += 1
            gp   += 1
        elif char == '0':
            gp   += 1
    return float(wins)/float(gp)

def calcOwp(team, mat):
    wps = []
    for i in range(len(mat)):
        if i != team and mat[team][i] != '.':
            result = mat[i][0:team]
            result.extend(mat[i][team+1:])
            wps.append(calcWp(result))
    return float(sum(wps))/float(len(wps))

def calcOowp(mat, team, owps):
    revised = []
    for i in range(len(mat[team])):
        if mat[team][i] != '.' and i != team:
            revised.append(owps[i])
    return float(sum(revised))/float(len(revised))

def calcRpi(numTeams, mat):
    wps   = []
    owps  = []
    oowps = []
    rpis  = []
    for i in range(len(mat)):
        wps.append(calcWp(mat[i]))
        owps.append(calcOwp(i, mat))
    for i in range(len(wps)):
        oowps.append(calcOowp(mat, i, owps))
        rpis.append(0.25 * wps[i] + 0.50 * owps[i] + 0.25 * oowps[i])
    stringResult = ''
    for r in rpis:
        stringResult += str(r) + '\n'
    return stringResult

filename = sys.argv[1]
f = open(filename, 'r')
testCases = int(f.readline().split()[0])
for i in range(testCases):
    numTeams = int(f.readline().split()[0])
    resultMatrix = []
    for j in range(numTeams):
        stats = list(rstrip(f.readline()))
        resultMatrix.append(stats)
    result = calcRpi(numTeams, resultMatrix)
    print("Case #" + str(i + 1) + ":\n" + result[0:len(result)-1])
f.close()
