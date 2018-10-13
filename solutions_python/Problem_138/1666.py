#!/usr/bin/env python
# coding: utf-8


#inputFile = open('D-small-attempt0.in')
inputFile = open('D-large-attempt0.in')
outputFile = open(inputFile.name[:-3] + '.out', 'w')

lines = [line.rstrip('\n') for line in inputFile]
inputFile.close()
casesLen = int(lines[0])


def parse_string(unParsed):
    return [float(item) for item in unParsed.split(' ')]
    pass


def findKenChosen(naomiChosen, ken):
    for blockK in ken:
        if blockK > naomiChosen:
            return blockK
    return ken[0]


def removeBlock(stack, block):
    return [x for x in stack if x != block]


def war(naomi, ken):
    result = 0
    for blockN in naomi:
        naomiChosen = blockN
        kenChosen = findKenChosen(naomiChosen, ken)

        naomi = removeBlock(naomi, naomiChosen)
        ken = removeBlock(ken, kenChosen)

        if naomiChosen > kenChosen:
            result += 1


            #print naomiChosen, kenChosen

    return result


def find_biger_nearest(i, naomi):
    for j in naomi:
        if j > i:
            return j
    return False
    pass


def deceitful_war(naomi, ken):

    result = 0
    for i in range(len(naomi)):
        naomiChosen = find_biger_nearest(ken[0], naomi)
        if not naomiChosen:
            naomiChosen = naomiTold = naomi[0]
        else:
            naomiTold = 2

        naomi = removeBlock(naomi, naomiChosen)

        kenChosen = findKenChosen(naomiTold, ken)
        ken = removeBlock(ken, kenChosen)

        if naomiChosen > kenChosen:
            result += 1

        print naomiChosen, naomiTold, kenChosen, '+' if naomiChosen > kenChosen else '-'
        print naomi, ken


    return result


for i in range(casesLen):
    print i + 1, '\n---'
    #print "'"+lines[i + 1]+"'"

    naomi = sorted(parse_string(lines[2::3][i]))
    ken = sorted(parse_string(lines[3::3][i]))

    print naomi, ken

    deceitfulResult = deceitful_war(naomi, ken)
    warResult = war(naomi, ken)

    print deceitfulResult, warResult
    result = "{} {}".format(deceitfulResult, warResult)
    outLine = "Case #{}: {}".format(i + 1, result)
    outputFile.write(outLine + "\n")
    print '\n'
    pass

outputFile.close()
