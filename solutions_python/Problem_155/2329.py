fin = open('A-small-attempt0.in.txt','r')

fout = open('output.txt', 'w')

numCases = int(fin.readline())

for cases in range(numCases):
    lst = list(map(int, fin.readline().split()))

    shyestLevel = lst[0]
    shyPersons = lst[1]

    addedPplNum = 0
    standingPpl = 0
    for shyLevel in range(shyestLevel + 1):
        if standingPpl < shyLevel:
            addedPplNum = addedPplNum + shyLevel - standingPpl
            standingPpl = standingPpl + shyLevel - standingPpl

        standingPpl = standingPpl + shyPersons // (10 ** (shyestLevel - shyLevel) ) % 10

    #print(shyestLevel, shyPersons, addedPplNum)

    fout.write("Case #" + str(cases+1) + ": "+ str(addedPplNum)+'\n')


fin.close()
fout.close()