from collections import defaultdict
import sys

def testCase(stalls, people):
    while people > 1:
        #print people
        #print stalls
        if stalls == 1:
            stalls = 0
            people -= 1
        elif stalls % 2 == 0:
            #stalls.extend([stalls[0]/2, (stalls[0]-1)/2])
            if people % 2 == 0:
                stalls = stalls/2
                people = (people )/2
            else:
                stalls = (stalls - 1)/2
                people = (people )/2
        else:
            stalls = stalls/2
            people = (people )/2

    #print people
    #print stalls
    #print stalls
    if stalls % 2 == 0:
        return [stalls/2, (stalls-1)/2]
    else:
        return [stalls/2, stalls/2]


testcount = int(sys.stdin.readline())
for i in range(testcount):
    line = sys.stdin.readline()
    values = map(int, line.split(" "))
    answer = testCase(values[0], values[1])
    #answer = testCase(int(line))
    print("Case #{}: {}".format(i+1, " ".join(map(str,answer))))
