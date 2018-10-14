import sys

name = "A-large"
path = ""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

testCases = int(input())

for testCase in range(1, testCases + 1):
    line = raw_input()
    line = line.split()

    dist = line[0]
    dist = float(dist)

    num_horse = line[1]
    horses = []
    m =0

    for x in range(int(num_horse)):
        horse = raw_input()
        horse = horse.split()
        pos = horse[0]
        pos = float(pos)
        speed = horse[1]
        speed = float(speed)
        horses.append([pos, speed])
        hours = (dist - pos)/speed
        m = max(m, hours)

    a = dist/m
    print "Case #" + str(testCase) +": " + "%.6f"%a
