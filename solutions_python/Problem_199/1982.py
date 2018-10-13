# Google code jam 2016
# Qualification Round - ..

import time

file_name = 'A-large';
input_file = open(file_name + '.in', 'r')
output_file = open(file_name  + '.out', 'w')

def main_function(caseNumber, pancakes, flipperSize):
    numberOfFlips = 0

    for index in range(0, len(pancakes)):
        if pancakes[index] == '-' and (index + flipperSize) < len(pancakes) + 1:
            pancakes[index:index+flipperSize] = flip(pancakes[index:index+flipperSize])
            print(''.join(pancakes))
            numberOfFlips += 1

    if '-' in pancakes:
        numberOfFlips = 'IMPOSSIBLE'

    print_result(caseNumber, numberOfFlips)

def flip(pancakes):
    flipped = []
    for pancake in pancakes:
        if pancake == '+':
            flipped.append('-')
        else:
            flipped.append('+')

    return flipped

def print_result(caseNumber, result):
    print("Case #{}: {}".format(caseNumber, result))

    output_file.write("Case #{}: {}\n".format(caseNumber, result))

def read_input_file():
    numberOfCases = int(input_file.readline())

    for caseNumber in range(1, numberOfCases + 1):
        # read input
        input_line = input_file.readline()
        (pancakes, flipper_size) = input_line.rstrip().split(' ')

        main_function(caseNumber, list(pancakes), int(flipper_size))

print('Starting ...')

start_time = time.time()

read_input_file()
input_file.close()
output_file.close()

end_time = round((start_time - time.time()) / 1000, 2)

print('Done! (Finished in {}ms)'.format(end_time))
