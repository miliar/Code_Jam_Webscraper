import sys
import math

def solveInterval(start, end):
    sqrtStart = math.ceil(math.sqrt(start))
    sqrtEnd = math.floor(math.sqrt(end)) + 1
    counter = 0
    for i in range(sqrtStart, sqrtEnd):
        if isPalindrome(i) and isPalindrome(i**2):
            counter += 1

    return counter

def isPalindrome(num):
    num = str(num)
    secondHalf = (len(num) // 2 if len(num) % 2 == 0 else (len(num) // 2) + 1)
    return (num[0:len(num) // 2] == num[secondHalf:])

f = open(sys.argv[1])
numOfCases = int(f.readline())
listOfCases = f.readlines()
f.close()

listOfAnswers = []

for case in listOfCases:
    start = int(case.split()[0])
    end = int(case.split()[1])
    listOfAnswers.append(solveInterval(start, end))

fout = open('output', 'w')

for ind, answer in enumerate(listOfAnswers):
    print('Case #' + str((ind + 1)) + ': ' + str(answer), file = fout)
    
fout.close()
