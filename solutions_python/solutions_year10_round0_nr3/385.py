import sys

def genTableRow(rideSize,groups, index):
    moneyMade = 0
    roomLeft = rideSize
    riding = {}

    while (roomLeft >= groups[index]):
        if (riding.has_key(index)):
                break

        roomLeft = roomLeft - groups[index]
        moneyMade = moneyMade + groups[index]
        riding[index] = 1;

        index = (index + 1) % len(groups)

    return (moneyMade,index)

def genTable(rideSize,groups):
    finalTable = []
    for i in range(0,len(groups)):
        finalTable.append(genTableRow(rideSize,groups,i))
    return finalTable

def calculateMoney(rideSize,rideRuns,groups):
    moneyMade = 0
    table = genTable(rideSize,groups)

    currentMoney = 0
    currentIndex = 0
    while (rideRuns > 0):
        rideRuns = rideRuns - 1
        (currentMoney, currentIndex) = table[currentIndex]
        moneyMade = moneyMade + currentMoney
    return moneyMade


def parse(filename):
    f = open(filename, 'r')
    cases = []
    
    number = int(f.readline())
    for i in range(number):
        rkn = f.readline().split()
        runs = int(rkn[0])
        size = int(rkn[1])
        groups = []
        
        groupsstr = f.readline().split()
        for grstr in groupsstr:
            groups.append(int(grstr))
        cases.append((runs,size,groups))
    return cases

def compute(cases):
    index = 1;
    for case in cases:
        runs = case[0]
        size = case[1]
        groups = case[2]

        money = calculateMoney(size,runs,groups)
        print "Case #" + str(index) + ": " + str(money)
        index = index + 1

cases = parse(sys.argv[1])
compute(cases)
