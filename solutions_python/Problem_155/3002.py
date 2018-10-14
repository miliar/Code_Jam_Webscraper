import sys

numcases = int(sys.stdin.readline())
input = []
for i in range(numcases):
    input.append(sys.stdin.readline())

cases = []
for line in input:
    tmp = line.strip('\n').split(' ')
    # cases.append([tmp[0], list(tmp[1])])
    cases.append(list(tmp[1]))

counter = 1
for case in cases:

    numfriends = 0
    clapping = 0
    # print case

    for i in range(len(case)):
        if clapping < i:
            numfriends += i-clapping
            clapping += i-clapping
        clapping += int(case[i])
    # print numfriends




    print "Case #" + str(counter) + ": " + str(numfriends)


    counter += 1