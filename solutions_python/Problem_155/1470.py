import sys

name = "A-large"
path = ""

sys.stdin = open(path + name +  ".in", "r")
sys.stdout = open(path + name + ".out", "w")


testCases = int(raw_input())

for testCase in range(1, testCases + 1):
    line = raw_input().split()
    n_str = int(line [0])
    shyness = line [1]
    total_up = int(shyness[0])
    total_miss = 0

    for i in range(1,n_str+1):
        miss = 0
        if (shyness [i] != 0):
            if (total_up < i):
                miss += i - total_up
                total_miss = total_miss + miss
        total_up = (total_up + int(shyness[i]) + miss)
    print "Case #" + str(testCase) + ": " + str(total_miss)
