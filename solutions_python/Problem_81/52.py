import numpy as np
import fileinput

import psyco
psyco.full()

def calcWPvec(wins,games):
    return wins.sum(axis=1)/games.sum(axis=1)

def calcOWPvec(wins,games):
    owpVec = []
    numTeams = len(wins[:,0])
    for i in range(numTeams):
        noUs = range(i)+range(i+1,numTeams)
        noMeGMat = games[np.ix_(noUs,noUs)]
        noMeWMat = wins[np.ix_(noUs,noUs)]
        allOWP = calcWPvec(noMeWMat,noMeGMat)
        myOWP = 0.0
        myOppCount = 0
        opponentsIdx = np.nonzero(games[:,i])
        for j in opponentsIdx[0]:
            myOppCount += 1
            if j < i:
                myOWP += allOWP[j]
            else:
                myOWP += allOWP[j-1]
        if myOppCount == 0:
            owpVec.append(0)
        else:
            owpVec.append(myOWP/myOppCount)
    return np.array(owpVec)

def calcOOWPvec(wins,games,OWPvec):
    oowpVec = []
    numTeams = len(wins[:,0])
    for i in range(numTeams):
        myOWP = 0.0
        myOppCount = 0
        opponentsIdx = np.nonzero(games[:,i])
        for j in opponentsIdx[0]:
            myOppCount += 1
            myOWP += OWPvec[j]
        if myOppCount == 0:
            oowpVec.append(0)
        else:
            oowpVec.append(myOWP/myOppCount)
    return np.array(oowpVec)
    

def calcRPI(wins,games):
    wp = calcWPvec(wins,games)
    #print "wp:",wp
    owp = calcOWPvec(wins,games)
    #print "owp:",owp
    oowp = calcOOWPvec(wins,games,owp)
    #print "oowp:",oowp
    return 0.25*wp+0.5*owp + 0.25*oowp

#print calcRPI(np.array([[0.0,1,1,0],
#                        [0,0,0,0],
#                        [0,1,0,1],
#                        [0,1,0,0]]),
#              np.array([[0.0,1,1,0],
#                        [1,0,1,1],
#                        [1,1,0,1],
#                        [0,1,1,0]]))
def cToG(c):
    if c == ".":
        return 0.0
    return 1.0

def cToW(c):
    if c in ".0":
        return 0.0
    return 1.0

def readMat(m):
    wins = []
    games = []
    for l in m:
        wins.append([cToW(x) for x in l.strip()])
        games.append([cToG(x) for x in l.strip()])
    return np.array(wins),np.array(games)

def solveCase(i,it):
    print "Case #%d:"%(i+1)
    numTeams = int(it.next())
    m = []
    for j in range(numTeams):
        m.append(it.next())
    wins,games = readMat(m)
    RPI = calcRPI(wins,games)
    for v in RPI:
        print v

def main():
    it = fileinput.input()
    numCases = int(it.next())
    for i in range(numCases):
        solveCase(i,it)

main()
