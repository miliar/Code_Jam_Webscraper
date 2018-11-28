def isPali(num):
    num = str(num)

    if len(num) <= 1:
        return True

    if num[0] != num[len(num) -1]:
        return False

    return isPali(num[1:-1])

def hasSquareRoot(num):
    if float(int(num ** .5 + .5)) == num ** .5:
        return True
    return False
    
def isFairAndSquare(num):
    if not hasSquareRoot(num):
        return False
        
    if isPali(num) and isPali(int(num ** .5)):
        return True
    return False
        
inData = [line.strip() for line in open('prob1.in')]

numCases = int(inData.pop(0))

for caseNum in xrange(1, 1 + numCases):
    values = [int(i) for i in inData.pop(0).split(' ')]
    start = values[0]
    stop = values[1]

    count = 0
    for value in range(start, stop + 1):
        if (isFairAndSquare(value)):
            count += 1

    print "Case #%s: %s" % (caseNum, count)
