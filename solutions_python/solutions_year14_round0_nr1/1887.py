#!/usr/bin/python

def get_cards():
    row = int(raw_input())
    vals = [raw_input().split(' ') for x in range(0, 4)]
    return set(vals[row - 1])
 
tc = int(raw_input())
for t in range(0, tc):
    c1 = get_cards()
    c2 = get_cards()
    c = c1 & c2

    if len(c) == 1:
        result = c.pop()
    elif len(c) == 0:
        result = "Volunteer cheated!"
    else:
        result = "Bad magician!"

    print "Case #%s: %s" % (t + 1, result)
