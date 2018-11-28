
for case in range(int(raw_input())):
    line = raw_input().split(' ')
    maxShyness = int(line[0])
    people = [int(num) for num in line[1]]

    nrFriends = 0

    standing = 0
    for shyness in range(maxShyness+1):
        nrPeople = people[shyness]
        if nrPeople == 0:
            continue
        if  shyness > standing:
            nrFriends += shyness - standing
            standing += shyness
        standing += nrPeople

    print "Case #%d: %s" % (case+1, nrFriends)
