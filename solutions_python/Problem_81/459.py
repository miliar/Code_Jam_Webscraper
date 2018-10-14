#!/usr/bin/python

import sys

def readint(f):
    return int(f.readline())

def getWins(char):
    if char == '.':
        return None
    if char == '1':
        return 1
    if char == '0':
        return 0

def numGames(arr):
    return len(filter(lambda x: x is not None, arr))

def numWins(arr):
    return sum(filter(lambda x: x == 1, arr))

def wp(arr):
    return float(numWins(arr))/float(numGames(arr))

def owp(teamInd,mat):
    return average([wp(opp[:teamInd] + opp[teamInd+1:]) for opp in opponents(teamInd,mat)])

def average(arr):
    return float(sum(arr))/float(len(arr))

def compute(mat):
    numTeams = float(len(mat))
    owps = []
    wps = []
    for team in mat:
        wps += [wp(team)]
    teamInd = 0
    for team in mat:
        owps += [owp(teamInd,mat)]
        teamInd += 1
    teamInd = 0
    for team in mat:
        oowp = average([owps[u] for u in oppIndices(teamInd,mat)])
        print 0.25 * wp(team) + 0.5 * owps[teamInd] + 0.25 * oowp
        teamInd += 1

def oppIndices(ind, mat):
    use = []
    for i in xrange(len(mat)):
        if i != ind and mat[ind][i] is not None:
            use += [i]
    return use

def opponents(ind, mat):
    use = oppIndices(ind, mat)
    delRows = [mat[u] for u in use]
    return delRows

if __name__ == "__main__":
    f = open(sys.argv[1], "r")
    numCases = readint(f)
    for i in xrange(numCases):
        numTeams = readint(f)
        mat = [[] for j in xrange(numTeams)]
        for j in xrange(numTeams):
            s = f.readline()
            mat[j] = map(getWins, s[:numTeams])
        print "Case #%d:" % ((i + 1))
        compute(mat)
