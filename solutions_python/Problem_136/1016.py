__author__ = 'mervinol'
#example

outputFile = open("CookieOut_Big.txt", "a")
inputFile = open("B-large.in", "r")
lines = inputFile.readlines()
inputFile.close()
TestCases = int(lines[0])
startLine = 1

def SolveProblem(linesfed):
    stash = 0.0
    factories = 0
    rateCombo = 2.0
    timeLapsed = 0.0
    costF,rateF,  X = tuple(float(x) for x in linesfed.split(" "))


    # print costF,rateF,  X
    homestretch = False
    while stash < X:
        timeStep = (min(costF-stash,X)/rateCombo)
        stashStep = rateCombo*timeStep
        timeLapsed += timeStep
        stash += stashStep

        # print "@%s: stash=%s" %(timeLapsed, stash)


        if stash >= costF and not homestretch:


            # #decide which option is best
            timeToFinish = (X-stash)/rateCombo
            timeWithFarm = (X-(stash-costF))/(rateCombo+rateF)
            # print "%s VS %s" %(timeToFinish, timeWithFarm)
            if timeToFinish > timeWithFarm:
                # print "BUY BUY BUY",
                factories +=1
                stash -= costF
                rateCombo += rateF
                # print "rate increased to", rateCombo
            else:
                # print "Stick it Out!"
                break

    timeLapsed += (X-stash)/rateCombo



    return timeLapsed


for case in range(TestCases):
    # print "Case #%s:" %(case+1),
    solution = SolveProblem(lines[startLine])
    print >>outputFile, "Case #%s:" %(case+1),
    print >> outputFile, "%.7f" % solution

    startLine += 1

outputFile.close()