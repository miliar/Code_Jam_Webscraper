"""
Allowable operations:
1) add a positive integer mote to the level
2) remove a mote

SOLUTION:
sort the array
if the current mote can be absorbed, do it
if not, add motes until it can be absorbed
    special: see if deletion of all from back will result in less mods
"""

inputFile = open('A-large.in', 'rU')
outputFile = open('A-large.out', 'w')

cases = int(inputFile.readline().strip())

for currentCase in xrange(1, cases + 1):
    # gathering input
    armin, noMotes = map(int, inputFile.readline().strip().split())
    moteSizes = map(int, inputFile.readline().strip().split())

    moteSizes = sorted(moteSizes)
    #DEBUG
##    print "Case #%d: Armin starts at %d" % (currentCase, armin)
##    print "Case #%d: " % currentCase + ' '.join(map(str, moteSizes))

    modifications = 0 # running tally of how many moves required to
    # make the level finishable
    arminNow = armin
    maximum = noMotes # upper bound, IMPORTANT 2
    for index in xrange(noMotes):
        if arminNow > moteSizes[index]:
            arminNow += moteSizes[index]
            # might need to do something to maximum here
            # continue # go on to next part of loop
        else: # not reachable
            # deletion method count
            deletions = noMotes - index # CHECK THIS PLEASE
            """CHECK THE ABOVE LINE"""
            maximum = min(maximum, modifications + deletions)
            # add motes to reach current
            tempNow = arminNow # this will be modified
            addTotal = 0 # theoretical modifications to reach next mote
            """EDGE CASE: it may be impossible to even add enough
            such that you can reach the end, e.g. [1,1,1,1],
            with armin = 1 is clearly impossible
            basically, this edge case only applies for armin = 1
            """
            while tempNow <= moteSizes[index] and addTotal <= 2000000:
                # second condition only for edge case
                # fast enough, since 2^20 > 10^6
                # counting intermediate motes added to reach the current mote
                tempNow = 2 * tempNow - 1
                addTotal += 1
            # compare the pair
            if deletions <= addTotal:
                modifications += deletions
                break # we're finished
            elif modifications + addTotal >= maximum:
                # where deletion was in fact the better option
                modifications = maximum
                break
            else:
                arminNow = tempNow # confirm change
                modifications += addTotal
                arminNow += moteSizes[index] # CRUCIAL
    # Output result
    print "Case #%d: %d" % (currentCase, modifications)
    outputFile.write("Case #%d: %d\n" % (currentCase, modifications))




        
inputFile.close()
outputFile.close()
