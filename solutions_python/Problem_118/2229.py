import math

def isPal(word):
    if len(word) == 0 or len(word) == 1:
        return True
    if word[0] == word[-1]:
        return isPal(word[1:-1])
    return False

def isOk(num):
    sq = int(math.sqrt(num))
    if sq * sq == num:
        return isPal(str(num)) and isPal(str(sq))
    return False

def readInput(f):
    sraw = f.readlines()
    noi = int(sraw[0][:-1])
    raw = []
    for one in sraw[1:]:
        raw.append(map(int, one.split()))
    return noi, raw

def testRange(case):
    count = 0
    for one in range(case[0], case[1]+1):
        if isOk(one):
            count += 1
    return count

f = open('C-small-attempt0.in')
noi, data = readInput(f)
n = 1
for case in data:
    print 'Case #' + str(n) + ': ' + str(testRange(case))
    n += 1
