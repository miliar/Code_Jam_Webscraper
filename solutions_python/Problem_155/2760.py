T = int(input())


def addFriends(sMax, shyness):
    count = 0
    friends = 0

    for i in range(0, sMax):
        count += shyness[i]

        if count < i+1:
            friends += ((i+1) - count)
            count += ((i+1) - count)

    return friends

#f = open('outOne.txt', 'w')
for i in range(1, T+1):

    inp = raw_input()
    shy = inp.split(" ")
    sMax = int(shy[0])
    S = shy[1]
    shyness = []
    for x in S:
        shyness.append(int(x))

    needed = addFriends(sMax, shyness)

    print 'Case #' + str(i) + ': ' + str(needed)
    #f.write('Case #' + str(i) + ': ' + str(needed) + '\n')

#f.close()