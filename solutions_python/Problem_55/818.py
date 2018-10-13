import sys

file = open(sys.argv[1], "r")
numberoftests = int(file.readline())
case = 1

def printCase(case, money):
    print "Case #%d: %d" % (case, money)

def runRollercoaster(runs, size, groups):
    money = 0
    for run in range(runs):
        riding = []
        while groups:
            if groups[0] + sum(riding) <= size:
                riding.append(groups.pop(0))
            else:
                break
        groups.extend(riding)
        money += sum(riding)
    return money

firstline = True
for line in file:
    split = line.split(" ")
    if firstline:
        runs = int(split[0])
        size = int(split[1])
        firstline = False
    else:
        groups = split
        for key in range(len(groups)):
            groups[key] = int(groups[key])
        firstline = True
        money = runRollercoaster(runs, size, groups)
        printCase(case, money)
        case = case + 1
