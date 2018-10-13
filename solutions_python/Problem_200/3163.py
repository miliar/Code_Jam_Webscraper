#!/usr/bin/python3

def isTidy(n):
    n = str(n)
    for i in range(0, len(n)-1):
        if n[i] > n[i+1]:
            return False
    return True

def findTidy(n):
    while not isTidy(n):
        nList = list(str(n))

        # Set all variables to integers
        for i in range(0, len(nList)):
            nList[i] = int(nList[i])

        # Decrease larger numbers until tidy
        for i in range(len(nList)-1, 0, -1):
            if nList[i-1] > nList[i]:
                for j in range(i, len(nList)):
                    nList[j] = 9
                nList[i-1] = max(0, nList[i-1] - 1)

        # Revert variables to string for conversion to integer
        for i in range(0, len(nList)):
            nList[i] = str(nList[i])
        n = int(''.join(nList))
    return n

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n = int(input())

    print("Case #{}: {}".format(i, findTidy(n)))
    # check out .format's specification for more formatting options

