i = open('A-small-attempt0.in', 'r')
cases = int(i.readline())
o = open('A-small-output.txt', 'w')


counter = cases
while counter > 0:
    counter -= 1
    solution = 0
    rawData = i.readline()
    rawPeople = rawData[2:-1]
    people = []
    for shygroup in range(0, len(rawPeople)):
        for person in range(1, int(rawPeople[shygroup]) + 1):
            people.append(shygroup)
    solved = False
    standing = 0
    while solved != True:
        tmpStand = standing
        for person in people:
            if tmpStand >= person:
                people.remove(person)
                standing += 1
        if standing == tmpStand:
            standing += 1
            solution += 1
        if people == []:
            solved = True
    o.write("Case #" + str(cases - counter) + ": " + str(solution) + "\n")

i.close()
o.close()