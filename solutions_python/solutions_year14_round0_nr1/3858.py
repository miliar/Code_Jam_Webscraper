#!/usr/bin/env python

import sys

input_file = open(sys.argv[1])
T = int(input_file.readline())

def read_arrangement(f):
    arrangement = []
    for _ in xrange(4):
        arrangement.append(set([int(c) for c in f.readline().strip().split()]))
    return arrangement

def read_answer(f):
    return int(f.readline())

def cards_moved_between(rows, arrangements):
    cards = []
    for card1 in arrangements[1][rows[1] - 1]:
        if card1 in arrangements[0][rows[0] - 1]:
            cards.append(card1)
    return cards
        

def cards_changed_in(row, arrangements):
    return 4 - len(arrangements[0][row - 1] & arrangements[1][row - 1])

for case in xrange(1, T + 1):
    answers = []
    arrangements = []
    answers.append(read_answer(input_file))
    arrangements.append(read_arrangement(input_file))
    answers.append(read_answer(input_file))
    arrangements.append(read_arrangement(input_file))

    solutions = cards_moved_between(answers, arrangements)

    if len(solutions) == 1:
        print "Case #%d: %d" % (case, list(solutions)[0])
    elif len((arrangements[1][answers[1] - 1] & arrangements[0][answers[0] - 1])) > 1:
        print "Case #%d: Bad magician!" % (case, )
    else:
        print "Case #%d: Volunteer cheated!" % (case, )
