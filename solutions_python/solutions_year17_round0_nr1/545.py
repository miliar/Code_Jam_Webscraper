import sys

numTests = int(sys.stdin.readline())
tests = []

def isAllFlipped(pancakes, i, j):
    for k in range(i, j):
        if(pancakes[k]=='-'):
            return False
    return True

# Read all tests
for i in range(numTests):
    t = sys.stdin.readline()
    s = t.split(' ')
    tests.append(s)

# Solve them
for i in range(numTests):
    s = tests[i]

    pancakes = list(s[0])
    pancakesLen = len(pancakes)
    fliperSize = int(s[1])

    # base case
    if fliperSize > pancakesLen:
        if isAllFlipped(pancakes, 0, pancakesLen):
            print 'Case #' + str(i+1) + ': 0'
        else:
            print 'Case #' + str(i+1) + ': IMPOSSIBLE'
        continue

    # tries to solve flipping from left to right
    totalFlips = 0
    for j in range(0, (pancakesLen-fliperSize+1)):
        if pancakes[j] == '-':
            totalFlips += 1
            for k in range(j, (j+fliperSize)):
                if pancakes[k] == '-':
                    pancakes[k] = '+'
                else:
                    pancakes[k] = '-'

    # check and print result
    if isAllFlipped(pancakes, (pancakesLen-fliperSize+1), pancakesLen):
        print 'Case #' + str(i+1) + ': ' + str(totalFlips)
    else:
        print 'Case #' + str(i+1) + ': IMPOSSIBLE'
