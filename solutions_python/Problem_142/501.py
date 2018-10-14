import sys

def findGroups(string):
    groups = []

    lastchar = None
    count = 0
    
    for char in string:
        if lastchar is None:
            lastchar = char
            count = 1
            continue

        if char != lastchar:
            groups.append((lastchar, count))
            count = 1
            lastchar = char
            continue

        if char == lastchar:
            count += 1

    return groups

def handleGroups(groups):
    length = None

    changes = 0
    
    for groupList in groups:
        if length is None:
            length = len(groupList)
            continue
        
        if len(groupList) != length:
            return False

    for groupIndex in range(0, length):
        currentGroups = [group[groupIndex] for group in groups]

        lastchar = None

        for group in currentGroups:
            if lastchar is None:
                lastchar = group[0]
                continue
            if group[0] != lastchar:
                return False

        minimum = None
        maximum = None
        
        for group in currentGroups:
            num = group[1]
            
            if num < minimum or minimum is None:
                minimum = num

            if num > maximum or maximum is None:
                maximum = num

        midpoint = int(sum([group[1] for group in currentGroups])/len(currentGroups))

        for group in currentGroups:
            num = group[1]

            changes += abs(midpoint - num)

    return changes

def handlestrings(strings):
    groups = [findGroups(string) for string in strings]
    return handleGroups(groups)


with open(sys.argv[-1], 'r') as infile:
    numcases = int(infile.readline())

    for x in range(0, numcases):
        numstrings = int(infile.readline())
        strings = [infile.readline() for y in range(0, numstrings)]
        result = handlestrings(strings)
        print "Case #{x}: {result}".format(x=x+1,result = result if result is not False else 'Fegla Won')
