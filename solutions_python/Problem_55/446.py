
FILE = open("C-small-attempt0.in","r")
OUTPUT = open("C-small-attempt0.out","w")

cases = FILE.readline()

def rideCoaster():
    global k
    global groups
    groupsOnCoaster = []
    numberOfRiders = 0
    while(len(groups) > 0 and numberOfRiders + groups[0] <= k):
        groupCount = groups.pop(0)
        numberOfRiders += groupCount
        groupsOnCoaster.append(groupCount)
    groups.extend(groupsOnCoaster)
    return numberOfRiders


for i in range(0,int(cases)):
    temp = FILE.readline().split(" ")
    temp2 = FILE.readline().split(" ")
    r = int(temp[0])
    k = int(temp[1]) 
    n = int(temp[2])
    groups = []
    for j in temp2:
        groups.append(int(j))
    moneyMade = 0
    for j in range(0,r):
        moneyMade += rideCoaster()
    OUTPUT.write('Case #' + str(i + 1) + ': ' + str(moneyMade) + '\n')
        
FILE.close()
OUTPUT.close()

