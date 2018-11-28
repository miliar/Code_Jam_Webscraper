#!/usr/bin/env python

"""
Google Code Jam 2014
Qualification round
Problem A. Magic Trick
"""

import sys
import argparse

class TestCase:
    pass

def process_command_line(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=argparse.FileType('r'),
                        help="Input file")
    args = parser.parse_args()

    return args

def process_input(args):
    casescount = int(args.filename.readline())
    testcases = []

    for i in range(1, casescount + 1):
        volunteer_row_1 = int(args.filename.readline())

        cards_1 = []
        for j in range(1, 4 + 1):
            cardline = args.filename.readline()
            cardline = cardline.split()
            cardline = map(int, cardline)
            cards_1.append(cardline)

        volunteer_row_2 = int(args.filename.readline())

        cards_2 = []
        for j in range(1, 4 + 1):
            cardline = args.filename.readline()
            cardline = cardline.split()
            cardline = map(int, cardline)
            cards_2.append(cardline)

        testcase = TestCase()
        testcase.volunteer_row_1, testcase.volunteer_row_2, testcase.cards_1, testcase.cards_2 = \
            volunteer_row_1, volunteer_row_2, cards_1, cards_2
        testcases.append(testcase)

    # for line in args.filename:
    #    buffer += line

    args.filename.close()

    return testcases

def magic_trick(testcase):
    # Find where all the cards from the volunteer's first row are in the second dealing
    deal2_rows = []

    for card in testcase.cards_1[testcase.volunteer_row_1 - 1]:
        for row in range(len(testcase.cards_2)):
            try:
                if testcase.cards_2[row].index(card) >= 0:
                    deal2_rows.append(row + 1)
                    # debug print str(card) + " found in " + str(row + 1)
            except ValueError:
                pass

    # check for cheating volunteer
    # criteria: none of the cards from the first row are in the second row
    if not testcase.volunteer_row_2 in deal2_rows:
        return "Volunteer cheated!"

    # check for bad magician
    # criteria: the cards in the first volunteer row should all be in separate rows in the second dealing
    if deal2_rows.count(testcase.volunteer_row_2) >= 2:
        return "Bad magician!"

    # Originally I thought I should return "bad magician" if the magician left open the possibility
    # that she'd be unable to identify the volunteer's card. My submitted answer was judged incorrect,
    # so I suspect in fact I'm only supposed to report "bad magician" if the magician cannot tell
    # which card is the volunteer's after the second answer.
    #deal2_rows.sort()
    #if deal2_rows[0] == deal2_rows[1] or deal2_rows[1] == deal2_rows[2] or deal2_rows[2] == deal2_rows[3]:
    #    return "Bad magician!"

    # determine card
    for card1 in testcase.cards_2[testcase.volunteer_row_2 - 1]:
        for card2 in testcase.cards_1[testcase.volunteer_row_1 - 1]:
            if card1 == card2:
                return str(card1)

    return "Error"

def main(argv=None):
    args = process_command_line(argv)
    # application code here, like:
    testcases = process_input(args)

    for t in range(len(testcases)):
        print "Case #" + str(t + 1) + ": " + str(magic_trick(testcases[t]))

    return 0        # success

if __name__ == '__main__':
    status = main()
    sys.exit(status)
