import sys

f = open(sys.argv[1])
testcasecount = int(f.readline())

for  testcase in range(testcasecount):
    dataset = f.readline()[:-1].split(" ")
    #print("Case #%d: " % (testcase+1))
    #print(dataset)
    C = float(dataset[0])
    F = float(dataset[1])
    X = float(dataset[2])


    #print(C, F, X)

    farmcount = 0
    buildtime = 0
    speed = 2
    prodtime = 0

    while True:
        besttime = prodtime
        prodtime = buildtime + (X / speed)

        if (prodtime > besttime) and (farmcount > 0):
            break
        #print("Farms: %d, speed: %f, totaltime: %f" % (farmcount, speed, prodtime))
        timetobuildfarm = C / speed
        buildtime += timetobuildfarm
        #print("   Time to build farm %d: %f" % (farmcount+1, timetobuildfarm))
        speed += F
        farmcount +=1
    print("Case #%d: %.7f" % (testcase+1, besttime))
