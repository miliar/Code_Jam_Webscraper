#!/usr/bin/python

import sys

if (len(sys.argv) < 2):
  print "Incorrect syntax"

try:
  infile = open(sys.argv[1], 'r')
  outfile = open(sys.argv[1]+".out", 'w')

  # Read in number of cases.
  n = int(infile.readline())

  for i in range(1, n+1):
    selectedrow1 = int(infile.readline())
    print "selectedrow1 = ", selectedrow1
    cardlayout1 = []
    for j in range(4):
      cardlayout1.append([int(x) for x in infile.readline().split()])
    print "cardlayout1 = ", cardlayout1
    selectedrow2 = int(infile.readline())
    print "selectedrow2 = ", selectedrow2
    cardlayout2 = []
    for j in range(4):
      cardlayout2.append([int(x) for x in infile.readline().split()])
    print "cardlayout2 = ", cardlayout2


    # Calculate the number of cards in selectedrow1 that match those in selectedrow2.
    nMatchingCards=0
    lastMatchingCard=-1
    for k in range(4):
      for m in range(4):
        if cardlayout1[selectedrow1-1][k] == cardlayout2[selectedrow2-1][m]:
          nMatchingCards += 1
          lastMatchingCard= cardlayout1[selectedrow1-1][k]

    if nMatchingCards == 0:
      answerstring="Volunteer cheated!"
    elif nMatchingCards == 1:
      answerstring=str(lastMatchingCard)
    elif nMatchingCards > 1:
      answerstring = "Bad magician!"
    else:
      print "Incorrect value for nMatchingCards"
    #

    formattedanswerstring = "Case #" + str(i) + ": " + answerstring
    print formattedanswerstring
    outfile.write(formattedanswerstring + "\n")

  infile.close()
  outfile.close()
except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
except:
  print "Unexpected error:", sys.exc_info()[0]
  raise
else:
  infile.close()
  outfile.close()
