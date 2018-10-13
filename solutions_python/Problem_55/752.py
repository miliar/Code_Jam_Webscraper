def main():
    ifile = open('input.txt', 'r')
    ofile = open('output.txt', 'w')

    num = int(ifile.readline().strip())
    for n in range(num):
        runs,size,numGroups = map(lambda x: int(x), ifile.readline().split(" "))
        groups = map(lambda x: int(x), ifile.readline().split(" "))
        ans = solve(runs,size,groups,numGroups)
        ofile.write("Case #%s: %s\n" % (n+1,ans))

    ifile.close()
    ofile.close()

def solve(runs,size,groups,numGroups):
    #do until we wrap back around to exactly the same situation
    rides = [] #each elements holds end $
    groupRides = [None for n in range(numGroups)]
    remainingrides = runs
    grp = 0 #the group at the front of the line to get on
    total = 0

    first = True
    startgrp = 0
    while remainingrides > 0:
        #break if its not none, because we've been to this group before
        if groupRides[grp] is not None:
            break

        numThisRide = 0
        startgrp = grp
        firstgrp = True
        while True:
            if numThisRide + groups[grp] <= size and (startgrp is not grp or firstgrp):
                numThisRide += groups[grp]
                grp = (grp + 1) % numGroups
            else:
                break
            firstgrp = False
        remainingrides -= 1
        total += numThisRide
        rides.append(total)
        groupRides[startgrp] = len(rides)-1
        first = False #to prevent us from thinking we've looped around on the very first one

    if remainingrides == 0:
        return total

    #figure out the number of rides in the repeat cycle
    r0 = grp
    rn = startgrp
    numrepeated = groupRides[rn] - groupRides[r0] + 1
    repeatedcost = rides[groupRides[rn]]
    if groupRides[r0] > 0: #if we didn't start at 0, remove the parts before we started repeating
        repeatedcost -= rides[groupRides[r0]-1]

    fullrepeats = remainingrides / numrepeated
    partial = remainingrides % numrepeated
    total += fullrepeats*repeatedcost
    if partial is not 0:
        total += repeatedcost - (rides[groupRides[rn]] - rides[partial+groupRides[r0]-1])

    return total

if __name__ == "__main__":
    main()
