testNumbers = 0
with open ('B-small-attempt0.in') as testFile:
  testNumbers = int(testFile.readline())
  for index in range(0, testNumbers):
    #print "\n\n"
    cookieRate = 2.0
    line = testFile.readline().split()
    C = float(line[0])
    F = float(line[1])
    X = float(line[2])
    #print C
    #print F
    #print X

    noFarmTimeCost = X/2.0

    #time to buy a farm + the new time cost with a farm
    oneFarmTimeCost = C/cookieRate + X/(F+cookieRate)

    xFarmTimeCost = []
    xFarmTimeCost.append(noFarmTimeCost)
    for i in range(1, 100000):
      timeCost = 0.0
      numberOfFarm = i
      #print "numberOfFarm : %d" %numberOfFarm
      #time cost of buying i number of cookie farm
      count = 0.0
      while numberOfFarm > 0: 
        timeCost += C/(cookieRate+count * F)
        #print "loop: %d" % index
        #print "count * F: %f" % (count * F)
        numberOfFarm -= 1
        count += 1.0
        #print count

      timeCost += X/(F*i + cookieRate)
      #print "timeCost : %f" % timeCost
      xFarmTimeCost.append(timeCost)
      if xFarmTimeCost[i] > xFarmTimeCost [i-1]:
        print "Case #%d: %.7f" % (index+1, xFarmTimeCost[i-1])
        break

