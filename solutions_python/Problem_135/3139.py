#!/usr/bin/python

import sys

def get_cards(fin, row):
    ret = None
    for i in range(4):
        s = fin.next()
        if i == row-1:
            ret = s[:-1].split(' ')
    return ret

with sys.stdin as fin:
    cases = int(fin.next())
    for i in range(cases):
        row1 = int(fin.next())
        possible1 = get_cards(fin, row1)
        row2 = int(fin.next())
        possible2 = get_cards(fin, row2)

        candidates = [card for card in possible1 if card in possible2]        
        print "Case #{}:".format(i+1), 
        if len(candidates) == 0:
            print "Volunteer cheated!"
        elif len(candidates) > 1:
            print "Bad magician!"
        else:
            print candidates[0]
