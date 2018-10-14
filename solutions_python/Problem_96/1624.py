file = open("sample")

def calc(line):
    items = line.split(' ')
    googlerCount = int(items.pop(0))
    surprises = int(items.pop(0))
    p = int(items.pop(0))
    items.sort();

    count = 0
    surpriseCount = 0

    for score in items:
        score = int(score)
        normal = getTriplet(score)
        surprising = getSurprising(score)
        if(normal >= p):
            count = count + 1
        elif(surprising >= p and surpriseCount < surprises):
            count = count + 1
            surpriseCount = surpriseCount + 1
    return count

def getTriplet(score):
    lower = score/3
    mod = score%3
    if mod == 0:
        return lower
    elif mod == 1 or mod == 2:
        return lower + 1

def getSurprising(score):
    if score == 0:
        return 0
    elif score == 1:
        return 1
    else:
        lower = (score-2)/3
        return lower + 2

lineNo = 0
while 1:
    line = file.readline()
    if not line:
        break
    pass
    line = line.replace('\n','')
    if lineNo == 0:
        testCount = line
    elif line != '':
        print 'Case #' + str(lineNo) + ': ' + str(calc(line))
    lineNo = lineNo + 1

