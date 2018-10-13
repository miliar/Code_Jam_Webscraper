import sys

file = open(sys.argv[1], "r")
numberoftests = int(file.readline())
case = 1

def printCase(number, light):
    if light == False:
        print "Case #%d: OFF" % number
    else:
        print "Case #%d: ON" % number

for line in file:
    split = line.split(" ")
    numberofsnappers = int(split[0])
    numberofsnaps = int(split[1])
    snappers = []
    for i in range(numberofsnappers):
        if snappers:
            snappers.append([False, False])
        else:
            snappers.append([True, False])
    
    for i in range(numberofsnaps):
        for snapper in snappers:
            if snapper[0] == True:
                snapper[1] = not snapper[1]
        power = True
        for snapper in snappers:
            snapper[0] = power;
            if snapper[0] and snapper[1]:
                power = True
            else:
                power = False
    printCase(case, snappers[-1][0] and snappers[-1][1])
    case = case + 1
