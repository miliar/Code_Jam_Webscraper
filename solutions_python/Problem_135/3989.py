#!/usr/bin/python

import sys

def main(argv):
    if len(argv) < 2:
            print "Please Provide filename!"
            sys.exit(1)

    input = open(argv[1], 'r')
    testCount = input.readline()

    cardMatrix1 = [[0]*3 for i in range(4)]
    cardMatrix2 = [[0]*3 for i in range(4)]

    for z in range(1,int(testCount)+1):
            firstAnswer = int(input.readline())
            for x in range(0,4):
                cardMatrix1[x] = input.readline().rstrip().split()
            secondAnswer = int(input.readline())
            for y in range(0,4):
                cardMatrix2[y] = input.readline().rstrip().split()
            solution = solveProblem(firstAnswer, secondAnswer, cardMatrix1, cardMatrix2)
            if solution == -1:
                print "Case #" + str(z) + ": Bad magician!"
            elif solution == -2:
                print "Case #" + str(z) + ": Volunteer cheated!"
            else:
                print "Case #" + str(z) + ": " + str(solution.pop())
                
def solveProblem(firstAnswer, secondAnswer, cardMatrix1, cardMatrix2):
    # possible answers
    pa1 = cardMatrix1[firstAnswer-1]
    pa2 = cardMatrix2[secondAnswer-1]

    result = set(pa1).intersection(set(pa2))
    if len(result) > 1:
        return -1
    elif len(result) == 0:
        return -2
    else:
        return result

if __name__ == "__main__":
    main(sys.argv)
