#! /usr/bin/python
import sys

INFILE= sys.argv[1]

with open(INFILE) as f:
  nTestCase = int( f.readline() )
  caseNo = 0
  while caseNo < nTestCase:
    deck1 = [[0 for x in xrange(4)] for x in xrange(4)]
    deck2 = [[0 for x in xrange(4)] for x in xrange(4)]

    card_row1 = int(f.readline().strip() )
    for i in xrange(4):
      deck1[i] = [int(x) for x in f.readline().split()]
    #print deck1
    card_row2 = int(f.readline().strip() )
    for i in xrange(4):
      deck2[i] = [int(x) for x in f.readline().split()]
    
    #print deck2;
    caseNo+=1
    found = 0
    found_card = -1;
    for card in deck1[card_row1 - 1]:
      if card in deck2[card_row2 - 1]:
        found_card = card
        found+=1
    
    if found == 1:
      print "Case #%s: %s"% (caseNo,found_card)
    elif found ==0:
      print "Case #%s: %s"% (caseNo,"Volunteer cheated!")
    else:
      print "Case #%s: %s"% (caseNo,"Bad magician!")