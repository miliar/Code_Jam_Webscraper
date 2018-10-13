def isTidy(integer): # Returns -1 if it's tidy, the position where it breaks down if it's not
    integer = str(integer)
    if int(integer) < 10:
        return -1

    for i in range(0,len(integer) - 1):
        if int(integer[i + 1]) < int(integer[i]):
            return i
    return -1

def putNines(integer, breakPoint):
    #print breakPoint
    intList = list(integer)
    #print breakPoint
    #print intList
    intList[breakPoint] = str(int(intList[breakPoint]) - 1)

    for i in range (breakPoint + 1, len(integer)):
        intList[i] = '9'
    #print intList
    lastInt = ''.join(intList)
    #print lastInt

    # If first item is 0, pop
    return int(lastInt)

# Open file
filepath = "B-large.in"
f = open(filepath, 'r')

integers = []

# Read input
i = 0
for line in f:
    # First line: Number of cases
    if i == 0:
        cases = int(line)
        i = i + 1
        continue
    # Next lines
    integers += [str(int(line))]

# SOLVE EACH CASE
solutions = []
caseNumber = 0
lastInt = 0
for intg in integers:
    #print "New integer"
    #print intg
    breakPoint = isTidy(intg)
    #print breakPoint

    if breakPoint == -1:
        #print intg
        solutions += [intg]
    else:
        # Check if there is a previous Number
        if breakPoint == 0: # No there isn't
#            if str(intg[0]) == 1:
#                lastInt = putNines(intg, breakPoint - i - 1)
#            else:
            lastInt = putNines(intg, 0)
        else: # Yes there is
            # Recurse
            for i in range (0, len(intg)):
                # Check if previous number is smaller
                current = intg[breakPoint - i]
                past = intg[breakPoint - i - 1]
                if (breakPoint - i - 1) < 0:
                    lastInt = putNines(intg, 0)
                    break
                #print past + " vs. " + current
                if int(past) < int(current): # Yes it is
                    lastInt = putNines(intg, breakPoint - i)
                    break
        if lastInt == 0:
            lastInt = putNines(intg, 0)
        solutions += [str(lastInt)]
    #print (lastInt)

# Output
i = 1
data = ''
for s in solutions:
    data += "Case #" + str(i) + ": " + str(s) + "\n"
    #print  "Case #" + str(i) + ": " + str(s) + "\n"
    i = i + 1


# Write
outputFile = 'b-large.txt'
f2 = open(outputFile, 'w')
f2.write(data)
f2.close()
