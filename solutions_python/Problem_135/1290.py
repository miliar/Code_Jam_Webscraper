#!/usr/bin/python

#Case #1: 7
#Case #2: Bad magician!
#Case #3: Volunteer cheated!
def test(choice, first, second, o, caseNum):
    fc = first[choice[0] - 1]
    sc = second[choice[1] - 1]

    found = 0
    selection = -1
    for x in fc:
        for y in sc:
            if x == y:
                found += 1
                selection = x
        if found > 1:
            break

    if found > 1:
        o.write("Case #" + str(caseNum) + ":" + " Bad magician!\n")
    elif found == 0:
        o.write("Case #" + str(caseNum) + ":" + " Volunteer cheated!\n")
    else:
        o.write("Case #" + str(caseNum) + ": " + str(selection) + "\n")

    

f = open("/Users/tony/Downloads/A-small-attempt0.in.txt")
i = f.readline()
o = open("a.out", 'w')

i = int(i)

for t in xrange(0, i):
    choice = []
    first = []
    second = []

    x = f.readline().split()
    y = int(x[0])
    choice.append(y)

    for k in xrange(0, 4):
        l = [int(z) for z in f.readline().split()]
        first.append(l)

    x = f.readline().split()
    y = int(x[0])
    choice.append(y)

    for k in xrange(0, 4):
        l = [int(z) for z in f.readline().split()]
        second.append(l)

    test(choice, first, second, o, t + 1)