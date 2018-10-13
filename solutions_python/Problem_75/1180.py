#-------------------------------------------------------------------------------
# Name:        B-small-0.py
# Purpose:     Google Code Jam
#
# Author:      Jakub Koba
#
# Created:     07-05-2011
# Copyright:   (c) Jakub Koba 2011
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import sys

def hasOpposition(elements,oppositions,let):
    for elem in elements:
        if (elem,let) in oppositions:
            return True
    return False

def resolve_case(case,counter):

    params = case.split(" ")

    #Combinations parsing
    combines = {}
    combinesCount = int(params[0])

    for combinePos in range(combinesCount):
        combine=params[combinePos+1]
        combines[(combine[0],combine[1])] = combine[2]
        combines[(combine[1],combine[0])] = combine[2]

    #Oppostions parsing
    oppositions = []
    oppoCount = int(params[1+combinesCount])

    for oppoPos in range(oppoCount):
        opposition = params[2+combinesCount + oppoPos]
        oppositions.append((opposition[0],opposition[1]))
        oppositions.append((opposition[1],opposition[0]))

    #Case parsing
    lettersCount = int(params[2+combinesCount+oppoCount])
    letters = params[3+combinesCount+oppoCount]

    elements = []

    for letNum in range(lettersCount):
        let = letters[letNum]

        if len(elements) > 0:
            if (elements[-1],let) in combines.keys():
                combined_letter =  combines[(elements[-1],let)]
                elements[-1]=combined_letter
            elif hasOpposition(elements,oppositions,let):
                elements = []
            else:
                elements.append(let)
        else:
            elements.append(let)

    print "Case #"+str(counter) + ":", "[" + ", ".join(elements) + "]"

def main():
    f = open(sys.argv[1])
    #f = open("B-test.txt")
    c_count=f.readline()
    for caseNum in range(int(c_count)):
        resolve_case(f.readline().rstrip(),caseNum+1)

if __name__ == '__main__':
    main()
