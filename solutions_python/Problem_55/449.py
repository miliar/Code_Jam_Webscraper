fileName = "C-small-attempt0"

inputFile = open( fileName + ".in", "r" )
outputFile = open( fileName + ".out", "w" )

numCases = int(inputFile.readline())

for caseNumber in range(1, numCases + 1):

  input_s = inputFile.readline()
  
  numRuns         = int(input_s.split()[0])
  coasterCapacity = int(input_s.split()[1])
  numGroups       = int(input_s.split()[2])
  
  groupQueue = inputFile.readline().split()

  groupQueue = [int(g) for g in groupQueue]

  currentLoad = 0
  currentSet  = []
  profit = 0
  
  for run_ix in range(numRuns):

    #print "run", run_ix
    #print "starting queue:"
    #print groupQueue

    # Load up
    while (currentLoad + groupQueue[0]) <= coasterCapacity:
      currentSet.append(groupQueue[0])
      currentLoad += groupQueue[0]
      groupQueue = groupQueue[1:]
      if len(groupQueue) == 0:
        break
    
    #print "loaded:"
    #print currentSet
    #print groupQueue
    
    profit += currentLoad
    
    # Unload
    groupQueue = groupQueue + currentSet;
    currentSet = []
    currentLoad = 0
    
    #print "unloaded:"
    #print groupQueue
    #print "profit", profit
    #print " "


  # Output the results
  outputFile.write( "Case #%d: %d\n" % (caseNumber, profit) )

# Close the streams
inputFile.close()
outputFile.close()
