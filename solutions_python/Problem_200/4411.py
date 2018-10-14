def getDigits(number):
    l = []
    num = number
    while num > 0:
        digit = num % 10
        num /= 10
        l.append(digit)
    return l[::-1]
    

def checkTidy(l):
    '''takes list of digits as input, checks tidiness as defined by GCJ'''
    sameCount = 0
    for i in xrange(len(l)-1):
        if l[i+1]<l[i]:
            return (False,i - sameCount)
        elif l[i+1] == l[i]:
            sameCount += 1
    return (True,0)

inpFile = open('B-small-attempt0.in', 'r')
try:
    t = int(inpFile.readline())
    for case in xrange(t):
        number = int(inpFile.readline())
        numlist = getDigits(number)
        tidiness = checkTidy(numlist)
        changeIndex = tidiness[1]
        if tidiness[0]:
            print 'Case #{}: {}'.format(case, number)
            continue
        elif numlist[-1] == 0:
            numlist[changeIndex] -= 1
            for j in xrange(changeIndex + 1, len(numlist)):
                numlist[j] = 9
            print 'Case #{}: {}'.format(case, int(''.join([str(x) for x in numlist])))
        else:
            numlist[changeIndex] -= 1
            numlist = [x if ind<=changeIndex else 9 for ind, x in enumerate(numlist)]
            print 'Case #{}: {}'.format(case, int(''.join([str(x) for x in numlist])))
except EOFError:
    pass
