import sys

masterSet = []

def generateSolutions(set, value, index):
    if len(set) == 0:
        global masterSet
        masterSet.append(value)
    for i in range(len(set)):
        testValue = value + set[i]
        newSet = set[0:i] + set[i+1:len(set)]
        generateSolutions(newSet, testValue, index+1)

fh = open(sys.argv[1], "r")
output = open("outputA.txt", "w")
lines = fh.readlines()
sets = int(lines[0])
for i in range(sets):
    output.write("Case #" + str(i + 1) + ": ")
    masterSet = []
    setInput =  str(lines[1 + i]).rstrip() + "0"
    checkValue = int(lines[1+i].rstrip())
    generateSolutions(setInput, "", 0)
    masterSet.sort(reverse=True)
    leastValue = int(masterSet[0])
    for value in masterSet:
        if int(value) > checkValue and int(value) < leastValue:
            leastValue = int(value)
    output.write(str(leastValue) + "\n")
output.close()
fh.close()
