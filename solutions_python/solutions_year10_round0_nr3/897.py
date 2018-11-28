f = open("C-small-attempt0.in", "r")

tcNumber =  int(f.readline())

a = 1
for _ in range(tcNumber):
    (maxPerDay, maxPeople, numOfGroup) = [int(i) for i in f.readline().split(" ")]
    groups = [int(i) for i in f.readline().split(" ")]
    money = 0
    
    for _ in range(maxPerDay):
        newGroups = []
        people = 0
        for i in groups:
            if (people + i) > maxPeople:
                break
            people = people + i
            newGroups.append(i)
        money = money + sum(newGroups)
        groups = groups[len(newGroups):] + newGroups
    print "Case #" + str(a) + ": " +  str(money)
    a = a + 1

f.close()
