#/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
from pprint import pprint

nb_tests = int(sys.stdin.readline())

for test in range(nb_tests):
    def read_row():
        "Read the row containing the answer"
        arr = []
        answer = int(sys.stdin.readline())
        for i in range(4):
            arr.append([int(card) for card in sys.stdin.readline().split(' ')])
        return arr[answer - 1]

    row1 = read_row()
    row2 = read_row()

    possible = []
    for card in row1:
        if card in row2:
            possible.append(card)

    if len(possible) == 1:
        res = possible[0]
    elif len(possible) == 0:
        res = "Volunteer cheated!"
    else: # len(possible) > 1
        res = "Bad magician!"

    print "Case #%s: %s" % (test + 1, res)
