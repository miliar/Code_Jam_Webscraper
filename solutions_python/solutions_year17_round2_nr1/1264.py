# GET FILE #
file = open("A-large.in").readlines()[1:]
outputFile = open("A.out","w")

### TIMES FUNCTION ###

def getTime(destination, position, speed):
    return (destination - position) / speed

def getSpeed(destination,time):
    return destination / time

# MAKE CASES #
cases = []
while file:
    cases.append(file[:int(file[0].split(" ")[1].strip())+1])
    for i in range(int(file[0].split(" ")[1].strip())+1):
        file.pop(0)
# DO EACH CASE #
caseCount = 1
for case in cases:
    destination = int(case[0].split(" ")[0])
    horses = case[1:]
    slowestTime = 0
    # FIND NEW SLOWEST HORSE #
    for horse in horses:
        if getTime(destination,int(horse.split(" ")[0]),int(horse.split(" ")[1])) > slowestTime:
            slowestTime = getTime(destination,int(horse.split(" ")[0]),int(horse.split(" ")[1]))
    # FIND TIME #
    outputFile.write("Case #" + str(caseCount) + ": " + str(getSpeed(destination,slowestTime)) + "\n")
    caseCount += 1
outputFile.close()