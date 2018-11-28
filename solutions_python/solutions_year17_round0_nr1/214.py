import sys

# Open file for processing
filename = sys.argv[1]
inputFile = open(filename, 'r')
lines = [l.rstrip('\n') for l in inputFile]
linesIter = iter(lines)
nCases = int(linesIter.next())


# Process each case
for iCase in range(1,nCases+1):

    # Solve problem
    inString = linesIter.next()
    vals = inString.split(" ")
    strArr = vals[0].strip()
    flipSize = int(vals[1])

    arr = [x == '+' for x in strArr]

    flipCount = 0
    for i in range(len(arr) - flipSize + 1):

        if not arr[i]:
            flipCount += 1
            for j in range(i, i+flipSize):
                arr[j] = not arr[j]

        
    allGood = True
    for x in arr:
        if not x:
            allGood = False


    if allGood:
        print("Case #{}: {}".format(iCase, flipCount))
    else:
        print("Case #{}: {}".format(iCase, "IMPOSSIBLE"))
