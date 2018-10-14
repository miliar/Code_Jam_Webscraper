import string

file_name = "disks.in"

disksInput = open(file_name, 'r')
data = string.split(disksInput.read().strip(), '\n')
numCases = int(data[0])


def countNumDisks(diskSize, disks):
    disks.sort()
    count = 0
    startPtr = 0
    endPtr = len(disks)-1
    while startPtr <= endPtr:
        count +=1
        if disks[startPtr] + disks[endPtr] <= diskSize:
            startPtr +=1
        endPtr -=1
    return count

index = 1
for case in range(1,numCases+1):
    numDisks, diskSize = [int(x) for x in string.split(data[index])]
    disks = [int(x) for x in string.split(data[index+1])]
    index +=2

    print "Case #" + str(case)+ ":", countNumDisks(diskSize, disks)
