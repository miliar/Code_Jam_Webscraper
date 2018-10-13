import sys, re
from fractions import Fraction

def getrpi(testcase):
    numteams = testcase[0]
    wincounts = testcase[1]
    losecounts = testcase[2]
    gameoutcomes = testcase[3]
    
    # get WPs
    WPs = []
    OWPs = []
    for i in range(numteams):
        WPs.append( (float(wincounts[i]) / (float(wincounts[i])+float(losecounts[i]))) )

        matchcount = 0
        accumowp = 0.0
        j = 0
        for match in gameoutcomes[i]:
            if match == '.': pass
            else:
                matchcount += 1
                if int(match) == 0: exclude = 1
                else: exclude = 0
                otherteamwp = float(wincounts[j] - exclude) / float(wincounts[j] + losecounts[j] - 1)
                accumowp += otherteamwp
                
            j += 1

        avgowp = (accumowp / float(matchcount))
        OWPs.append(avgowp)
        

    OOWPs = []
    for i in range(numteams):
        matchcount = 0
        accumoowp = 0.0
        j = 0
        for match in gameoutcomes[i]:
            if match == '.': pass
            else:
                matchcount += 1
                accumoowp += OWPs[j]
            j += 1

        avgoowp = accumoowp / float(matchcount)
        OOWPs.append(avgoowp)

    RPIs = []
    for i in range(numteams):
        RPIs.append(0.25*WPs[i] + 0.5*OWPs[i] + 0.25*OOWPs[i]  )

    return RPIs


def processtestcases():
    numtestcases = int(sys.stdin.readline().rstrip())
    testcases = []


    # pre-proc: counts and pos-array
    wincounts = []
    losecounts = []
    gameoutcomes = []

    for i in range(numtestcases):
        numteams = int(sys.stdin.readline().rstrip())

        j = 0
        wincounts = []
        losecounts = []
        gameoutcomes = []
        for j in range(numteams):
            teamrow = sys.stdin.readline().rstrip()
            wincounts.append( teamrow.count("1") )
            losecounts.append( teamrow.count("0") )
            gameoutcomes.append(teamrow)

        # 3 items
        testcases.append([numteams, wincounts, losecounts, gameoutcomes])

    return testcases


if __name__ == "__main__":
    testcases = processtestcases()
    #print str(testcases)
    i = 1
    for testcase in testcases:
        print "Case #"+str(i)+":"
        rpidata = getrpi(testcase)
        for teamrpi in rpidata:
            print str(teamrpi)
        i += 1





