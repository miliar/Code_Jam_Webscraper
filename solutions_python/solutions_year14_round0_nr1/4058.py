# -*- encoding: utf-8 -*-

"""
Google Code Jam 2014
QR
A : Magic Trick
"""

import numpy as np

import sys
import ipdb

with open(sys.argv[1], 'r') as f:
    tc_input = f.readlines()
raw_input = lambda: tc_input.pop(0)

T = int(raw_input())
#print("input : {} test cases".format(T))

def tc():
    guess1 = int(raw_input())
    cards = []
    for i in range(4):
        cards.append(map(int,raw_input().split()))
    cards1 = np.array(cards)

    guess2 = int(raw_input())
    cards = []
    for i in range(4):
        cards.append(map(int,raw_input().split()))
    cards2 = np.array(cards)

    row1 = cards1[guess1-1,:]
    row2 = cards2[guess2-1,:]

    """
    print guess1
    print cards1
    print row1
    print guess2
    print cards2
    print row2
    """

    # Choosen cards
    cc = np.intersect1d(row1, row2)
    nbcc = len(cc)

    if nbcc == 1:
        return cc[0]
    elif nbcc > 1:
        return 'Bad magician!'
    elif nbcc == 0:
        return 'Volunteer cheated!'

    ipdb.set_trace()


for t in range(T):
    print "Case #{}: {}".format(t+1, tc())
