#!/usr/bin/env python

T = int(raw_input().strip())

def get_row(answer):
    rows = []
    for i in range(0, 4):
        row = raw_input().strip().split()
        rows.append(row)
    return rows[answer-1]

for i in range(1, T+1):
    print ("Case #%d:" % i),
    ans1 = int(raw_input().strip())
    row1 = get_row(ans1)
    ans2 = int(raw_input().strip())
    row2 = get_row(ans2)

    possible_cards = list(set(row1) & set(row2))
    if len(possible_cards) == 0:
        print "Volunteer cheated!"
    elif len(possible_cards) == 1:
        print possible_cards[0]
    else:
        print "Bad magician!"