#!/usr/bin/env python

from __future__ import print_function

import sys
from collections import defaultdict


def main(*args):
    global translation

    if(len(args) < 2):
        print("Usage: %s <input file>" % args[0])

    filename = args[1]
    input_file = open(filename, "rb")
    output_file = open(filename+".out", "wb")

    try:
        in_str = input_file.readline().strip()
    except:
        print("Premature end of input")

    T = int(in_str)
    for k in range(T):
        row1_str = input_file.readline()
        row1 = int(row1_str[0])
        cards1 = list()
        for i in range(4):
            card_num_strs = input_file.readline().split()
            card_row = list()
            for card_num_str in card_num_strs:
                card_row.append(int(card_num_str))
            cards1.append(card_row)

        row2_str = input_file.readline()
        row2 = int(row2_str[0])
        cards2 = list()
        for i in range(4):
            card_num_strs = input_file.readline().split()
            card_row = list()
            for card_num_str in card_num_strs:
                card_row.append(int(card_num_str))
            cards2.append(card_row)

        appeared_cards = defaultdict(int)
        for card_num in cards1[row1-1]:
            appeared_cards[card_num] += 1
        for card_num in cards2[row2-1]:
            appeared_cards[card_num] += 1

        chosen_card = -1    # -1: volunteer cheated
        for (appeared_card, num_times) in appeared_cards.iteritems():
            if(num_times == 2):
                if(chosen_card == -1):
                    chosen_card = appeared_card
                else:
                    chosen_card = -2    # bad magician

        if(chosen_card == -1):
            print("Case #%d: Volunteer cheated!" % (k+1), file=output_file)
        elif(chosen_card == -2):
            print("Case #%d: Bad magician!" % (k+1), file=output_file)
        else:
            print("Case #%d: %d" % (k+1, chosen_card), file=output_file)

    input_file.close()
    output_file.close()


if(__name__ == "__main__"):
    sys.exit(main(*sys.argv))

