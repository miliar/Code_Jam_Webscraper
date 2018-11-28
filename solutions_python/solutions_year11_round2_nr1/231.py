'''
Jirasak Chirathivat
'''
import os
import os.path
import sys
import math

sys.setrecursionlimit(1000000000)

#### CHANGE HERE ####
#globals()['happy'] = {}
filename = 'A-large.in'

#### CHANGE HERE ####

def solve(teams):
    percentages = [0.0] * len(teams)
    percentages2 = [0.0] * len(teams)
    opPercentages = [0.0] * len(teams)
    opopPercentages = [0.0] * len(teams)
    rpi = [0.0] * len(teams)
    plays = []
    for i in range(len(teams)):
        plays.append([])
    
    for i in range(len(teams)):
        t = teams[i]
        played = 0.0
        wins = 0.0
        for y in range(len(t)):
            ops = t[y]
            if ops == '.':
                continue
            if ops == '1':
                wins += 1
            played += 1
            plays[i].append(y)
            percentages[i] = wins/played
            percentages2[i] = (wins, played)
    
    # for each team, calculate opponent scores
    for i in range(len(teams)):
        opPer = 0.0
        for j in range(len(plays[i])):
            op = plays[i][j]
            if teams[op][i] == '1':
                opPer += (percentages2[op][0] - 1) / (percentages2[op][1] - 1) 
            else:
                opPer += (percentages2[op][0]) / (percentages2[op][1] - 1)
        opPercentages[i] = opPer / len(plays[i])
        
    for i in range(len(teams)):
        opPer = 0.0
        for j in range(len(plays[i])):
            op = plays[i][j]
            opPer += opPercentages[op]
        opopPercentages[i] = opPer / len(plays[i])
    
    #print percentages, opPercentages, opopPercentages
        
    for i in range(len(teams)):
        rpi[i] = (0.25 * percentages[i]) + (0.5 * (opPercentages[i])) + (0.25 * (opopPercentages[i]))
    return '\n' + '\n'.join([('%.12f' % x )for x in rpi])


if __name__ == '__main__':    
    afile = file(filename)
    aread = afile.readlines()
    afile.close()
    
    out = file('out.txt', 'w')
    
    aread = [x.strip() for x in aread]
    
    numcase = int(aread[0])
    
    line = 1
    
    #happy = createHappy()
    
    for i in range(1, numcase + 1):
        
        #### CHANGE HERE ####
        N = int(aread[line])
        teams = aread[line+1:line+1+N]
        line += 1 + N
        #### CHANGE HERE

        #result = process(i, caseData)
        result = solve(teams)
        print >> out, 'Case #%s: %s' % (i,  result)
        print 'Case #%s: %s' % (i,  result)
    
    out.close()
