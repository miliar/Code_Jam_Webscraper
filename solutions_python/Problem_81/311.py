def crash():
    assert 1==2     

def percentage(arrayWins):
    wins = arrayWins.count('1')
    losses = arrayWins.count('0')
    return float(wins)/(wins+losses)
    
def average(arrayWins):
    return float(sum(arrayWins))/len(arrayWins)
    
    
fileLoc = '/Users/alarobric/Downloads/'
#fileLoc += 'A-small-attempt0'
#fileLoc += 'A-test'
fileLoc += 'A-large'
f = open(fileLoc+'.in', 'r')
g = open(fileLoc+'.out', 'w')
 
cases = int(f.readline())
 
for i in range (1, cases + 1):
    N = int(f.readline())
    #N teams
    winPerc = []
    winPercAgainst = [[] for j in range(N)]
    owp = []
    oowp = []
    rpi = []
    wins = []
    
    for j in range(N):
        line = [c for c in f.readline().strip()]
        wins.append(line)
    #print wins
    
    for k, teamWins in enumerate(wins):
        #print teamWins
        winPerc.append(percentage(teamWins))
        for j in range(N):
            if teamWins[j] == '.':
                winPercAgainst[j].append('.')
            else:
                tempTeamWins = teamWins[:]
                tempTeamWins.pop(j)
                #print "k", k, j, tempTeamWins, percentage(tempTeamWins)
                winPercAgainst[j].append(percentage(tempTeamWins))
    for winPercAgainstSub in winPercAgainst:
        #print "a", winPercAgainstSub
        for bob in range(winPercAgainstSub.count('.')):
            winPercAgainstSub.remove('.')
        owp.append(average(winPercAgainstSub))
        
    for k, teamWins in enumerate(wins):
        oowpTmp = []
        for j in range(N):
            if teamWins[j] == '1' or teamWins[j] == '0':
                oowpTmp.append(owp[j])
        oowp.append(average(oowpTmp))
        rpi.append(0.25 * winPerc[k] + 0.50 * owp[k] + 0.25 * oowp[k])
    
                
        
    #print "end"
    #print winPerc
    #print owp 
    #print oowp   
    #print rpi
    
    
    output = "Case #" + str(i) + ": " + "\n"
    for k in range(N):
        output += str(rpi[k]) + "\n"
    print output
    g.write(output)
    
#2
#3
#.10
#0.1
#10.
#4
#.11.
#0.00
#01.1
#.10.