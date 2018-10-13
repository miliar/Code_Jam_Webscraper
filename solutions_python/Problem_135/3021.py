
f = open('A-small-attempt0.in')

numCases = int(f.readline())

for i in xrange(numCases):
    row1 = []
    row2 = []

    ans1 = (int(f.readline()))
    for j in xrange(4):
        row1.append(f.readline().strip().split(' '))

    ans2 = (int(f.readline()))
    for j in xrange(4):
        row2.append(f.readline().strip().split(' '))

    choice1 = row1[ans1 - 1]
    choice2 = row2[ans2 - 1]

    matches = 0
    find = []
    for x in choice1:
        for y in choice2:
            if x == y:
                matches += 1
                find.append(x)

    answer = None
    if matches == 1:
        answer = find[0]
    elif matches == 0:
        answer = "Volunteer cheated!"
    elif matches > 1:
        answer = "Bad magician!"

    print "Case #{0}: {1}".format(i + 1, answer)



