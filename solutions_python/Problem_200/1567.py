import os, sys;
# I was going to use this to match the output to the file name, but since the same
# source will be used for practice, small and large inputs I changed my mind.
#fileName = os.path.basename(__file__).split('.')[0]

fileName = 'B-large'
print 'Running problem ' + fileName
inputFile = open(fileName + '.in', 'r')
outputFile = open(fileName + '.out', 'w')

# Writes answers for each case to terminal and to output file.
def writeAnswer(case, answer):
    line = 'Case #' + str(case + 1) + ': ' + str(answer)
    print line
    outputFile.write(line + "\n")

# The first line of every program is the number of cases.
cases = int(inputFile.readline())
print str(cases) + ' cases'

# Attempts to make a number tidier by choosing the next smaller number that might
# be tidy. Returns False if the number is already tidy. This will definitely
# return a tidy number after
def fixDigits(digits):
    for digit in range(len(digits) - 1):
        if int(digits[digit]) > int(digits[digit + 1]):
            if (digits[digit] == '0'):
                digits[digit - 1] = str(int(digits[digit - 1]) - 1)
                digits[digit] = '9'
            else:
                digits[digit] = str(int(digits[digit ]) - 1)
            for rest in range(digit + 1, len(digits)):
                digits[rest] = '9'
            return True
    return False

# Put the solution logic in a function so that variables we define will be local to the solution logic.
def solveProblem():
    for case in range(cases):
        print 'Solving case ' + str(case + 1)
        n = inputFile.readline().strip()
        digits = list(n)
        print digits
        i = 0
        while fixDigits(digits) and i <= len(n):
            # Uncomment to watch each change.
            print str(i) + ' ' + str(digits)
            # In case my logic in fixDigits is incorrect, increment this counter
            # to end the loop
            i += 1

        # Apparently python handles arbitrary sized ints so there is no risk of overflow here.
        # Casting to int removes leading '0's.
        writeAnswer(case, int(''.join(digits)))

solveProblem()
