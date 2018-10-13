#!/usr/bin/python

T = int(raw_input().strip())


def read_cards():
    cards = []
    for i in xrange(4):
        cards.append([int(_) for _ in raw_input().strip().split()])
    return cards


for case in xrange(T):
    result = None
    
    ans = int(raw_input().strip())
    cards = read_cards()
    
    ans2 = int(raw_input().strip())
    cards2 = read_cards()
    
    same = 0
    card = None
    for c in cards[ans-1]:
        if c in cards2[ans2 - 1]:
            same += 1
            card = c
    
    if same is 0:
        result = "Volunteer cheated!"
    elif same is 1:
        result = str(card)
    else:
        result = "Bad magician!"
    
    print "Case #%s: %s" % (str(case+1), result)