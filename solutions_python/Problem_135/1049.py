#!/usr/bin/python

# Magic trick solver for Google Code Jam
# Emilio Unda <unda91@gmail.com>
#
#

import sys


FAIL_STRING = "Bad magician!"
CHEAT_STRING = "Volunteer cheated!"

NUM_ROWS = 4

def magic(infilename, outfilename):
    file = open(infilename, 'r')
    out = open(outfilename, 'w')
    line = ""

    testcases = int( file.readline().strip() )

    # cycle through all of the test cases 
    for i in range(testcases):

        answer1 = int( file.readline().strip() )
        # cycle through the 4 rows
        for j in range(NUM_ROWS):
            line = file.readline()
            if answer1 == j+1 :
                # we only read the column the volunteer selected
                cards = line.split()

        # we go to the second case
        answer2 = int( file.readline().strip() )
        # cycle through the 4 rows
        for j in range(NUM_ROWS):
            line = file.readline()
            if answer2 == j+1 :
                # we only read the column the volunteer selected
                cards2 = line.split()
                
        # get all possible anwsers
        answers = possible_cards(cards, cards2)

        # start output
        out.write("Case #" + str(i+1) + ": ")
        # do corresponding output
        print str(answers)
        if len(answers) == 0 :
            out.write(CHEAT_STRING + "\n")
        elif len(answers) > 1 :
            out.write(FAIL_STRING + "\n")
        else :
            out.write(str(answers[0]) + "\n")
    #end for testcases
    return
#end magic


def possible_cards(cards1, cards2) :
    result = []
    for c in cards1:
        if c in cards2:
            result.append(c)
    return result


def main(argv):
    magic(argv[1], argv[2])
    return


if __name__ == "__main__" :
    main(sys.argv)
