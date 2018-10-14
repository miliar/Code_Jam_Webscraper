import os
import prime

x = 1024124214811
print prime.isPrime(x)


def get_empty_spots(case):
    empty_spots = 0
    for row in case:
        for spot in row:
            if spot == '?':
                empty_spots += 1
    return empty_spots


def fill_row(row):
    for i in xrange(1, len(row)):
        if row[i - 1] != '?' and row[i] == '?':
            row = row[0:i] + row[i - 1] + row[i + 1:]

    for i in xrange(len(row) - 2, -1, -1):
        if row[i + 1] != '?' and row[i] == '?':
            row = row[0:i] + row[i + 1] + row[i + 1:]

    return row


def get_solutions(cases):
    for case in cases:
        for i in xrange(0, len(case)):
            case[i] = fill_row(case[i])
        for i in xrange(1, len(case)):
            if case[i][0] == '?' and case[i - 1][0] != '?':
                case[i] = case[i - 1]
        for i in xrange(len(case) - 2, -1, -1):
            if case[i][0] == '?' and case[i + 1][0] != '?':
                case[i] = case[i + 1]
    return cases


def do():
    with open('input.txt') as input_file:
        testCases = input_file.readlines()
    numTestCases = testCases[0]
    testCases.remove(numTestCases)
    output_filename = 'output.txt'
    if os.path.exists(output_filename):
        os.remove(output_filename)

    cases = []
    while len(testCases) > 0:
        start = testCases.pop(0)
        num_rows, size_row = start.split(" ")
        case = []
        for _ in xrange(0, int(num_rows)):
            line = testCases.pop(0)
            case.append(line)
        cases.append([x.strip() for x in case])

    solutions = get_solutions(cases)

    with open(output_filename, 'a') as output_file:
        for i in xrange(0, len(solutions)):
            output_file.write('Case #' + str(i + 1) + ':\n')
            for line in solutions[i]:
                output_file.write(line + '\n')


do()
