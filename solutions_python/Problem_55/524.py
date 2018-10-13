inputfile = open("C-small-attempt1.in", "r")
outputfile = open("Output.txt", "w")
cases = int(inputfile.readline())
trials = 1

def moneymade(runs, capacity, groups, grouplist):
    currentruns = 0
    moneymade = 0
    groupposition = 0
    while currentruns < runs:
        currentcapacity = 0
        riders = []
        while currentcapacity <= capacity and len(grouplist) > 0:
            try:
                if currentcapacity + grouplist[groupposition] <= capacity:
                    currentcapacity += grouplist[groupposition]
                    riders.append(grouplist[groupposition])
                    groupposition += 1
                else: break
            except: break
        for rider in riders:
            grouplist.append(rider)
        moneymade += currentcapacity
        currentruns += 1
    return moneymade

while trials <= cases:
    print "TRIAL: " + str(trials)
    RkN = inputfile.readline().split()
    GrP = inputfile.readline().split()
    GrP2 = []
    for x in GrP:
        GrP2.append(int(x))
    outputfile.write("Case #" + str(trials) + ": " + str(moneymade(int(RkN[0]), int(RkN[1]), int(RkN[2]), GrP2)) + "\n")
    trials += 1
print "DONE"
outputfile.close()