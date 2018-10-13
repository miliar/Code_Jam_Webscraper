#!/usr/bin/python

import sys

if (len(sys.argv) < 2):
  print "Incorrect syntax"

try:
  infile = open(sys.argv[1], 'r')
  outfile = open(sys.argv[1]+".out", 'w')

  # Read in number of cases.
  n = int(infile.readline())

  # Iterate through the cases.
  for i in range(1, n+1):

    blockCount = int(infile.readline())

    naomiBlocks = [float(x) for x in infile.readline().split()]
    kenBlocks = [float(x) for x in infile.readline().split()]
    naomiBlocks.sort()
    kenBlocks.sort()
    naomiWarBlocks = list(naomiBlocks)
    naomiDeceitfulWarBlocks = list(naomiBlocks)
    kenWarBlocks = list(kenBlocks)
    kenDeceitfulWarBlocks = list(kenBlocks)

    # Optimal War.
    naomiWarScore = 0
    kenWarScore = 0
    for roundNumber in range(blockCount):
      # Naomi always choses smallest block when playing war.
      naomiChosen = naomiWarBlocks[0]
      del naomiWarBlocks[0]
      # If Ken has blocks that are heavier than Naomi's, he chosen the lighest of those.
      # Otherwise he choses his lightest block.
      for j in range(len(kenWarBlocks)):
        if kenWarBlocks[j] > naomiChosen:
          del kenWarBlocks[j]
          kenWarScore += 1
          break
        #
        if j == (len(kenWarBlocks)-1):
          del kenWarBlocks[0]
          naomiWarScore += 1
          break
        #
      #
    #

    # Optimal Deceitful War.
    naomiDeceitfulWarScore = 0
    kenDeceitfulWarScore = 0

    # Calculate how many of Naomi's block are heavier than Ken's.
    for roundnumber in range(blockCount):
      if naomiDeceitfulWarBlocks[len(naomiDeceitfulWarBlocks)-1] > kenDeceitfulWarBlocks[len(kenDeceitfulWarBlocks)-1]:
        naomiDeceitfulWarScore += 1
        del naomiDeceitfulWarBlocks[len(naomiDeceitfulWarBlocks)-1]
        del kenDeceitfulWarBlocks[len(kenDeceitfulWarBlocks)-1]
      else:
        kenDeceitfulWarScore +=1
        del naomiDeceitfulWarBlocks[0]
        del kenDeceitfulWarBlocks[len(kenDeceitfulWarBlocks)-1]
    #

#    for roundnumber in range(blockCount):
#      # Naomi forces Ken to use his heaviest blocks, while playing her lightest ones.
#
#      # If Ken has blocks that are heavier than Naomi's, he chosen the lighest of those.
#      # Otherwise he choses his lightest block.
#      for j in range(len(kenDeceitfulWarBlocks)):
#        if kenDeceitfulWarBlocks[j] > naomiChosen:
#          del kenDeceitfulWarBlocks[j]
#          kenDeceitflWarScore += 1
#          break
#        #
#        if j == (len(kenDeceitfulWarBlocks)-1):
#          del kenDeceitfulWarBlocks[0]
#          naomiDeceitfulWarScore += 1
#          break
#        #
#      #
#    #

    answerstring= str(naomiDeceitfulWarScore) + " " + str(naomiWarScore)

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
