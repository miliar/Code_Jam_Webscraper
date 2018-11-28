# roller coaster

import psyco
psyco.full()

# open files
fIn = open("input.txt")
fOut = open("output.txt", "w")

# get count
count = int(fIn.readline())

# do each line
for i in range(count):
    (rollerRuns, Kapacity, NumberOfPeople) = [int(x) for x in fIn.readline().split(' ')]
    peopleQueue = [int(x) for x in fIn.readline().split(' ')]

    currentPos = 0
    runCount = 0
    moneyMade = 0

    print rollerRuns, Kapacity, NumberOfPeople

    while runCount < rollerRuns:
        qcount = 0
        seated = 0
        runCount = runCount + 1
        while qcount < len(peopleQueue) and seated + peopleQueue[currentPos] <= Kapacity:
            seated = seated + peopleQueue[currentPos]
            currentPos = (currentPos+1) % len(peopleQueue)
            qcount = qcount + 1
        moneyMade = moneyMade + seated
        print seated, "!"

    fOut.write("Case #{0}: {1}\n".format(i+1, moneyMade))
    fOut.flush()
