#!/usr/bin/python

"""
Mousetrap problem solution
(GCJ 2008, Round 1B)
Author: madrezaan
"""

import sys

# open input file
if len(sys.argv) == 2 and sys.argv[1] != '--help':
    in_file = open(sys.argv[1])
else:
    print "Usage: mousetrap.py <input file>"
    sys.exit(0)

# get number of cases
num_cases = int(in_file.readline())

# begin prosessing cases
for cur_case in range(num_cases):

    # get number of cards
    k = int(in_file.readline())

    # generate perfect deck
    deck = map(lambda(x): None, range(k + 1))
    empty = map(lambda(x): x + 1, range(k))
    cur_card = 1
    cur_indice = 0
    empty_indice = -1
    reveal = 0
    while cur_card <= k:
        empty_indice = (empty_indice + cur_card) % len(empty)
        deck[empty[empty_indice]] = cur_card
        del empty[empty_indice]
        empty_indice -= 1
        cur_card += 1
           
    # get indices
    print "Case #%d:" % (cur_case + 1,),
    indices_str = in_file.readline().split(" ")
    n = int(indices_str[0])
    for i in range(1, n + 1):
        if i == n:
            print deck[int(indices_str[i])]
        else:
            print deck[int(indices_str[i])],
    del deck
    del empty

in_file.close()
