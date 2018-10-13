def getUntidyDigit(n):
    prevDigit = ''
    for i, digit in enumerate(str(n)):
        if prevDigit > digit: return len(str(n)) - i -1
        prevDigit = digit

    return -1

def getPreviousTydyNumber(n):
    while True:
        digit = getUntidyDigit(n)
        if digit < 0: return n
        n = FastGoBack(n,digit) #Originally tryied substracting by 1, but takes forever. Meade this 'fast go-backer' isntead

def FastGoBack(n,digit):
    '''This function aims to go back to a previous number, by substracting directly from the digit indicated
       and turning all the right-hand numbers to 9'''
    scale = 10**(digit+1)
    nToKeep = n // scale
    nToKeep -= 1
    nToKeep *= scale
    nToKeep += int('9'*(digit+1))
    return nToKeep


def solver():
    output = []

    casesToSolve = int(input())
    for i in range(1, casesToSolve+1):
        tidyNumber = getPreviousTydyNumber(int(input()))
        output.append('Case #%s: %s' % (i, tidyNumber))

    print('\n'.join(output))


solver()
