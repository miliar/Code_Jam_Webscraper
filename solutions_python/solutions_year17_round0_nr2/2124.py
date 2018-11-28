# Google code jam 2016
# Qualification Round - ..

import time
import math

file_name = 'B-large';
input_file = open(file_name + '.in', 'r')
output_file = open(file_name  + '.out', 'w')

def main_function(caseNumber, number):
    print_result(caseNumber, findTidy(number))

def findTidy(number):
    while (number > 0):
        # print(number)
        tidy = checkTidy(number)
        if tidy == 0:
            return number
        number = number - (number % pow(10,tidy)) - 1
    return 0

def checkTidy(number):
    # print(number)
    previousDigit = 10
    skipped = 0
    wrong = 0
    while (number > 0):
        lastDigit = number % 10
        if lastDigit > previousDigit:
            wrong = skipped
        previousDigit = lastDigit
        if number > 100000:
            number = int(str(number)[:-1])
        else:
            number = math.floor(number / 10)

        skipped = skipped + 1

    return wrong


def print_result(caseNumber, result):
    print("Case #{}: {}".format(caseNumber, result))

    output_file.write("Case #{}: {}\n".format(caseNumber, result))

def read_input_file():
    numberOfCases = int(input_file.readline())

    for caseNumber in range(1, numberOfCases + 1):
        # read input
        number = int(input_file.readline().rstrip())
        main_function(caseNumber, number)

print('Starting ...')

start_time = time.time()

read_input_file()
input_file.close()
output_file.close()

end_time = round((start_time - time.time()) / 1000, 2)

print('Done! (Finished in {}ms)'.format(end_time))
