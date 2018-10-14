# inits and returns a list with numStalls + 2 elems
# each elem is [(bool)occupied, (int)Ls, (int)Rs]
def initStallArr(numStalls):
    stallArr = []
    
    # add left guard
    stallArr.append([True, -1, -1])
    
    # add correct Ls and Rs for unoccupied stalls
    for i in xrange(numStalls):
        currStall = i + 1
        Ls = currStall - 1 # distance to leftmost stall
        Rs = numStalls - currStall # dist to rightmost
        stallArr.append([False, Ls, Rs])

    # add right guard
    stallArr.append([True, -1, -1])

    return stallArr

# Finds which stall the new person will enter
# Returns the index of the stall
def findWhichStall(stallArr):
    maxOfMin = -1 # current best results
    argMaxOfMin = [] # indices of all stalls achieving those results

    # relevant to those stalls achieving maxOfMin
    maxOfMax = -1
    argMaxOfMax = -1

    # find maxOfMin and maxOfMax
    for i in xrange(len(stallArr)):
        currStall = stallArr[i]
        if(not currStall[0]): # stall is unoccupied
            Ls = currStall[1]
            Rs = currStall[2]
            currMin = min(Ls, Rs)
            currMax = max(Ls, Rs)
            if(currMin > maxOfMin): # reset
                maxOfMin = currMin
                argMaxOfMin = [i]
                maxOfMax = currMax
                argMaxOfMax = i
            elif (currMin == maxOfMin): # add to argmax and check maxOfMax
                argMaxOfMin.append(i)
                if(currMax > maxOfMax):
                    maxOfMax = currMax
                    argMaxOfMax = i

    # find stall to enter
    stallToEnter = -1
    if(len(argMaxOfMin) == 1): # enter stall with maxOfMin
        stallToEnter = argMaxOfMin[0]
    else:
        stallToEnter = argMaxOfMax

    return stallToEnter

# Updates stallArr to add a person at stallIdx
# ie changes stallArr[stallIdx][0] to False and updates Ls and Rs
# for all other unoccupied stalls where needed
def updateStalls(stallArr, stallIdx):

    # update stalls to left of stallId (ie possibly update their Rs)
    for i in xrange(stallIdx):
        currStall = stallArr[i]
        if(not currStall [0]): # only update unoccupied stalls
            oldRs = currStall[2]
            distToNew = stallIdx - i - 1 # num stalls between
            if(distToNew < oldRs):
                stallArr[i][2] = distToNew

    # update stall at stallIdx
    stallArr[stallIdx][0] = True

    # update stalls to right of stallId (ie possibly update their Ls)
    for i in xrange(len(stallArr) - stallIdx - 1):
        currIdx = i + stallIdx + 1
        currStall = stallArr[currIdx]
        oldLs = currStall[1]
        distToNew = currIdx - stallIdx - 1 # num stalls between
        if(distToNew < oldLs):
            stallArr[currIdx][1] = distToNew

# simulates numPeople going into numStalls + 2 stalls with guards starting in
# in box end stalls
# returns max(Ls,Rs) and min(Ls,Rs) for the last stall entered
def simulateStalls(numStalls, numPeople):
    stallArr = initStallArr(numStalls)
    stallIdx = -1 # id of last stall entered
    for i in xrange(numPeople):
        stallIdx = findWhichStall(stallArr)
        updateStalls(stallArr, stallIdx)

    lastStallEntered = stallArr[stallIdx]
    Ls = lastStallEntered[1]
    Rs = lastStallEntered[2]
    lastMax = max(Ls, Rs)
    lastMin = min(Ls, Rs)
    return lastMax, lastMin


# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  numStalls, numPeople = [int(s) for s in raw_input().split(" ")]
  lastMaxOfMax, lastMaxOfMin = simulateStalls(numStalls, numPeople)
  # Output: Case #x: y z, where x is the test case number (starting from 1), 
  # y is max(LS, RS), and z is min(LS, RS)
  print "Case #{}: {} {}".format(i, lastMaxOfMax, lastMaxOfMin)
  # check out .format's specification for more formatting options