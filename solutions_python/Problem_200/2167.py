# returns a list of all digits in N, in correct order
def getDigList(N):
    digList = []
    while(N > 0):
        digList.append(N % 10)
        N /= 10
    digList.reverse()
    return digList

# Loops through digList from left to right. If any consecutive elems
# are in decreasing order, updates the list from that point on
# to the next non decreasing number
# ie if digList is [2,2,1,1] will detect a decreasing pair at indices 1 and 2
# and update to [2,1,9,9]
# returns True if an update was made, false otherwise
def tidyUpdate(digList):
    for i in xrange(len(digList) - 1):
        firstElem = digList[i]
        secondElem = digList[i + 1]
        if(secondElem < firstElem):
            numToRight = len(digList) - i - 1 # number of digits right of i
            digList[i+1:] = [9]*numToRight
            digList[i] -= 1
            if(i == 0 and digList[i] == 0):
                digList.remove(0)
            return True
    return False

# turns digList back into an int
def listToInt(digList):
    total = 0
    for i in xrange(len(digList)):
        total *= 10
        total += digList[i]
    return total


# returns the last tidy number before N
def findLastTidy(N):
    digList = getDigList(N)
    # loop until the nums in the list represent a tidy number then return it
    while(True):
        if(not tidyUpdate(digList)): # returns true if something updated
            break
    return listToInt(digList)


# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  N = int(raw_input())  # read a list of integers, 2 in this case
  lastTidy = findLastTidy(N)
  print "Case #{}: {}".format(i, lastTidy)
  # check out .format's specification for more formatting options