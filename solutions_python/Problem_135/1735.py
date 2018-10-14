#!/usr/bin/env python
# coding: utf-8


inputFile = open('A-small-attempt0.in')
#inputFile = open('A-large-attempt0.in')
outputFile = open(inputFile.name[:-3] + '.out', 'w')

lines = [line.rstrip('\n') for line in inputFile]
inputFile.close()
casesLen = int(lines[0])


def parse_string(unParsed):
    return [int(item) for item in unParsed.split(' ')]
    pass


def solve(firstAnswer, firstArrange, secondAnswer, secondArrange):
    firstRow = firstArrange[firstAnswer - 1]
    secondRow = secondArrange[secondAnswer - 1]
    result = list(set(firstRow) & set(secondRow))

    if len(result) == 1:
        result=result[0]
    elif len(result) > 1:
        result='Bad magician!'
    else :
        result='Volunteer cheated!'
    return result


for i in range(casesLen):
    print i + 1, '\n---'
    #print "'"+lines[i + 1]+"'"

    firstAnswer = int(lines[1::10][i])
    firstArrange = [parse_string(lines[2::10][i]),
                    parse_string(lines[3::10][i]),
                    parse_string(lines[4::10][i]),
                    parse_string(lines[5::10][i])]

    secondAnswer = int(lines[6::10][i])

    secondArrange = [parse_string(lines[7::10][i]),
                     parse_string(lines[8::10][i]),
                     parse_string(lines[9::10][i]),
                     parse_string(lines[10::10][i])]
    #items = parse_string(lines[3::3][i])

    print firstAnswer, firstArrange, secondAnswer, secondArrange

    result = solve(firstAnswer, firstArrange, secondAnswer, secondArrange)
    print result
    outLine = "Case #{}: {}".format(i + 1, result)
    outputFile.write(outLine + "\n")
    print '\n'
    pass

outputFile.close()
