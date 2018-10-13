from collections import defaultdict
import sys

def testCase(pancakes, size):
    #if set(pancakes) == set("+")
    #    return depth
    flips = 0
    pancakes = list(pancakes)
    while "-" in pancakes:
        index = pancakes.index('-')
        if index + size > len(pancakes):
            #print pancakes
            return "IMPOSSIBLE"
        for i in range(size):
            if pancakes[index + i] == "-":
                pancakes[index + i] = "+"
            else:
                pancakes[index + i] = "-"
        #print pancakes
        flips += 1
    return flips


testcount = int(sys.stdin.readline())
for i in range(testcount):
    line = sys.stdin.readline()
    #print line
    pancakes = line.split(" ")[0]
    size = line.split(" ")[1]
    answer = testCase(pancakes, int(size))
    #answer = testCase(map(int, ))
    #answer = testCase(int(line))
    print("Case #{}: {}".format(i+1, answer))
