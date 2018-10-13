#!/usr/bin/env python

import sys

x = 'X'
o = 'O'
wild_card = 'T'

sys.stdin = file("a-input")
sys.stdout = file("a-output", "w")

input_count = int(raw_input())

for instance in range(input_count):
    is_full = True
    board = {}
    for r in range(4):
        row = raw_input().strip()
        for c, col in enumerate(row):
            board[(r, c)] = col
            if col == ".":
                is_full = False
    try:
        raw_input()
    except EOFError:
        pass

    winner = wild_card
    # check rows
    for row in range(4):
        last_seen = ''
        num_found = 0
        for col in range(4):
            char = board[(row, col)]
            if char == last_seen or char == wild_card or last_seen == '':
                num_found += 1
                if char != wild_card:
                    last_seen = char
            else:
                continue
            if num_found == 4 and (last_seen == x or last_seen == o):
                winner = last_seen

    for col in range(4):
        last_seen = ''
        num_found = 0
        for row in range(4):
            char = board[(row, col)]
            if char == last_seen or char == wild_card or last_seen == '':
                num_found += 1
                if char != wild_card:
                    last_seen = char
            else:
                continue
            if num_found == 4 and (last_seen == x or last_seen == o):
                winner = last_seen

    last_seen = ''
    num_found = 0
    for row, col in zip(range(4), range(4)):
        char = board[(row, col)]
        if char == last_seen or char == wild_card or last_seen == '':
            num_found += 1
            if char != wild_card:
                last_seen = char
        else:
            continue
        if num_found == 4 and (last_seen == x or last_seen == o):
            winner = last_seen

    last_seen = ''
    num_found = 0
    for row, col in zip(range(4), range(3, -1, -1)):
        char = board[(row, col)]
        if char == last_seen or char == wild_card or last_seen == '':
            num_found += 1
            if char != wild_card:
                last_seen = char
        else:
            continue
        if num_found == 4 and (last_seen == x or last_seen == o):
            winner = last_seen

    if winner == x or winner == o:
        print "Case #%i: %s won" % (instance + 1, winner)
    elif is_full:
        print "Case #%i: Draw" % (instance + 1)
    else:
        print "Case #%i: Game has not completed" % (instance + 1)
