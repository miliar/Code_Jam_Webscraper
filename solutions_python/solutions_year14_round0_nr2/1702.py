#!/usr/bin/env python
# coding: utf-8


inputFile = open('B-small-attempt0.in')
#inputFile = open('B-large-attempt0.in')
outputFile = open(inputFile.name[:-3] + '.out', 'w')

lines = [line.rstrip('\n') for line in inputFile]
inputFile.close()
casesLen = int(lines[0])


def parse_string(unParsed):
    return [float(item) for item in unParsed.split(' ')]
    pass


def solve(data):
    price = data[0]
    profit = data[1]
    goal = data[2]
    farms = 0

    fastest = goal / 2

    while True:

        time = i = 0
        for i in range(farms):
            need = price / (2 + profit * i)
            time += need
            #print need, time

        time += goal / (2 + profit * farms)
        farms += 1

        if fastest < time:
            break

        fastest = time

    return fastest


for i in range(casesLen):
    print i + 1, '\n---'
    print parse_string(lines[i + 1])
    result = solve(parse_string(lines[i + 1]))
    print result
    outLine = "Case #{}: {}".format(i + 1, result)
    outputFile.write(outLine + "\n")
    print '\n'
    pass

outputFile.close()
