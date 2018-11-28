__author__ = 'CharlesT'

#....
# written as of 9:43

def getAnswer(r1, a1, r2, a2):
    """
    Returns string with desired message
    Takes in an index (0 = start) for r1 and r2
    Takes in int[][] arrangements a1, a2
    """
    candidates1 = set(a1[r1]) #4 possible from answer 1
    candidates2 = set(a2[r2])
    common = candidates1.intersection(candidates2)
    l = len(common)
    if l == 0:
        return "Volunteer cheated!"
    elif l > 1:
        return "Bad magician!"
    else: #only one value
        return str(common.pop()) #TOCHK: pop?

def parseIntsInArray(array):
    return [int(elem) for elem in array ]

numCases = int(raw_input())
for case in xrange(1, numCases+1): #TOCHK: range?
    whichRow1 = int(raw_input())
    arrangement1 = [parseIntsInArray(raw_input().split(' ')) for i in xrange(4)] #TOCHK: split
    whichRow2 = int(raw_input())
    arrangement2 = [parseIntsInArray(raw_input().split(' ')) for i in xrange(4)]
    print "Case #{}: {}".format(case, getAnswer(whichRow1-1, arrangement1, whichRow2-1, arrangement2))
