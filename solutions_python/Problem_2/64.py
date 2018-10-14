inputFileName = "B-large.in"
outputFileName = "B-large.out"

def solveCase(fileIn) :
    import time
    import datetime
    T = int(fileIn.readline())
    NA, NB = (int(x) for x in fileIn.readline().split())
    schedule = []
    for i in range(NA) :
        departure, arrival = (int(x.split(':')[0])*60 + int(x.split(':')[1]) for x in fileIn.readline().split())
        schedule.append((departure, arrival, 'A'))
    for i in range(NB) :
        departure, arrival = (int(x.split(':')[0])*60 + int(x.split(':')[1]) for x in fileIn.readline().split())
        schedule.append((departure, arrival, 'B'))
    schedule.sort()
    counters = {'A' : 0, 'B' : 0}
    stacks = {'A' : [], 'B' : []}
    opposite = {'A' : stacks['B'], 'B' : stacks['A']}
    for trip in schedule :
        origin = trip[2]
        stack = stacks[origin]
        if not stack or stack[0] > trip[0]:
            stack.append(0)
            stack.sort()
            counters[origin] += 1
        stack.pop(0)
        opposite[origin].append(trip[1] + T)
        opposite[origin].sort()
    return "%d %d" % (counters['A'], counters['B'])

def main() :
    import sys
    fileIn = open(inputFileName)
    if outputFileName == "stdout" :
        fileOut = sys.stdout
    else :
        fileOut = open(outputFileName, "w")
    N = int(fileIn.readline())
    for i in range(N) :
        fileOut.write("Case #%d: " % (i+1))
        fileOut.write(solveCase(fileIn))
        fileOut.write("\n")
    fileIn.close()
    if outputFileName != "stdout":
        fileOut.close()

if __name__== "__main__" :
    main()
