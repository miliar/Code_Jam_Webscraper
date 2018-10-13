# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
def findLargeSpace(bathList):
    max = [-1,-1] #s_index,size
    listSize = len(bathList)
    searchBool = False
    count = 0
    s_index = 0
    for i in xrange(0,listSize):
        if not searchBool and bathList[i] == 0: # first search empty stall
            searchBool = True
            s_index = i
            count = 1
        elif searchBool and bathList[i] == 0: # searching empty stalls
            count += 1
        elif searchBool and bathList[i] == 1: # end empty stalls
            # compare max and initialize
            if max[1] < count:
                max = [s_index, count]
            count = 0
            searchBool = False
    if max[1] < count:
        max = [s_index, count]
    return max

def findSlAndSr(bathlist, stallIndex):
    left = 0
    right = 0
    startIndex = stallIndex - 1
    # find Stall Left
    for i in xrange(startIndex, -1, -1):
        if bathlist[i] == 0:
            left += 1
        else:
            break

    # find Stall Right
    startIndex = stallIndex + 1
    for i in xrange(startIndex,len(bathlist)):
        if bathlist[i] == 0:
            right += 1
        else:
            break

    return [left, right]

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n, k = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    bathroom = [0] * n
    stall = 0
    for j in xrange(1,k + 1):
        stallRange = findLargeSpace(bathroom)
        stall = stallRange[0] + (stallRange[1]/2)
        bathroom[stall] = 1

    leftRight = findSlAndSr(bathroom,stall)

    print "Case #{}: {} {}".format(i, max(leftRight), min(leftRight))
  # check out .format's specification for more formatting options
