from Solve import *

def standingOvation(args):
    totalS, countsS = args[0].split(" ")
    total = int(totalS) + 1
    counts = [int(elem) for elem in countsS]
    
    totalUp = counts[0]
    totalFriends = 0
    for shyLevel in xrange(1, total):
        nPeople = counts[shyLevel]
        nPeopleMissing = shyLevel - totalUp
        if nPeopleMissing > 0:
            totalFriends += nPeopleMissing
            totalUp += nPeopleMissing
        totalUp += nPeople
    return totalFriends
    
solveF("F:\ProgramiranjeOstalo/GCJ/q2015/A-large.in", standingOvation, 1)