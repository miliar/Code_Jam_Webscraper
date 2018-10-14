import math
f = open('A-small-attempt1.in', 'r')
numCases = int(f.readline())
x = 1
while x <= numCases:
    line = f.readline()
    num, den = line.split('/')
    ans = float(num)/float(den)
    check = 1
    divides = 0
    possible = math.log(float(den), 2)
    if int(possible) != possible:
        print "Case #" + str(x) + ": impossible"
        x += 1
        continue
    while divides < 41:
        if ans >= check:
            break
        check /= 2.0
        divides += 1
    if divides == 41:
        print "Case #" + str(x) + ": impossible"
    else:
        print "Case #" + str(x) + ": " + str(divides)
    x += 1