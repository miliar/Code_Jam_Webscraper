from collections import defaultdict
import sys
debug = False
def testCase(p, groups):
    if debug: print p
    if debug: print groups
    transformedGroups = [0,0,0,0]
    for i in groups:
        transformedGroups[i % p] += 1





    if debug: print transformedGroups
    if p == 2:
        count = 0
        matches = transformedGroups[0]
        if debug: print matches
        count += matches
        transformedGroups[0] -= matches

        matches = transformedGroups[1]/2
        if debug: print matches
        count += matches
        transformedGroups[1] -= matches
        transformedGroups[1] -= matches

        #If there is anything left
        if transformedGroups[1]:
            count +=1

        return count

    if p == 3:
        count = 0
        matches = transformedGroups[0]
        count += matches
        transformedGroups[0] -= matches

        matches = min(transformedGroups[2], transformedGroups[1])
        count += matches
        transformedGroups[2] -= matches
        transformedGroups[1] -= matches

        matches = transformedGroups[1]/3
        if debug: print matches
        count += matches
        transformedGroups[1] -= matches * 3

        matches = transformedGroups[2]/3
        if debug: print matches
        count += matches
        transformedGroups[2] -= matches * 3

        if debug: print transformedGroups
        #If there is anything left
        if transformedGroups[1] or transformedGroups[2]:
            count +=1

        return count

    if p == 4:
        count = 0
        matches = transformedGroups[0]
        count += matches
        transformedGroups[0] -= matches

        matches = min(transformedGroups[3], transformedGroups[1])
        count += matches
        transformedGroups[3] -= matches
        transformedGroups[1] -= matches

        matches = transformedGroups[2]/2
        if debug: print matches
        count += matches
        transformedGroups[2] -= matches
        transformedGroups[2] -= matches

        if transformedGroups[3] >= 2 and transformedGroups[2] == 1:
            count += 1
            transformedGroups[3] -= 2
            transformedGroups[2] -= 1

        if transformedGroups[1] >= 2 and transformedGroups[2] == 1:
            count += 1
            transformedGroups[1] -= 2
            transformedGroups[2] -= 1

        matches = transformedGroups[1]/4
        if debug: print matches
        count += matches
        transformedGroups[1] -= matches * 4

        matches = transformedGroups[3]/4
        if debug: print matches
        count += matches
        transformedGroups[3] -= matches * 4


        if debug: print transformedGroups
        #If there is anything left
        if transformedGroups[1] or transformedGroups[2] or transformedGroups[3]:
            count +=1


        return count



testcount = int(sys.stdin.readline())
for i in range(testcount):
    line = sys.stdin.readline()
    n,p = map(int, line.split(" "))


    line = sys.stdin.readline()
    groups = map(int, line.split(" "))
    answer = testCase(p, groups)
    print("Case #{}: {}".format(i+1, answer))
