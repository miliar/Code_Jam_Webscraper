'''
author             Alex Vilanova (alexvilanovab@gmail.com)
problem            Qualification Round 2017 - B - Tidy Numbers
problem_url        https://code.google.com/codejam/contest/3264486/dashboard#s=p1
python_version     3.5.2
usage              python b.py inputFile outputFile
'''

# import libraries
import sys, datetime


# solve function
def solve(lastNumber):
    for number in range(lastNumber, 0, -1):
        numberDigits = list(str(number))
        numberDigitsSort = list(str(number))
        numberDigitsSort.sort()
        if numberDigits == numberDigitsSort:
            return number

# main function
def main():

    # start time
    startTime = datetime.datetime.now()

    # open input and output files
    inputFile = open(sys.argv[1], 'r')
    outputFile = open(sys.argv[2], 'w')

    # get cases
    cases = int(inputFile.readline())

    # loop through cases
    for case in range(1, cases + 1):

        # set up test case variables
        lastNumber = int(inputFile.readline())

        # set up output
        outputData = 'Case #{0}: {1}'.format(case, solve(lastNumber))

        # write and print output
        outputFile.write(outputData + '\n')
        print(outputData)

    # close input and output files
    inputFile.close()
    outputFile.close()

    # print elapsed time
    print('Elapsed time: {0}'.format(datetime.datetime.now() - startTime))


# start script
if __name__ == '__main__':
    main()
