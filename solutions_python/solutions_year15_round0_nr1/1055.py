import sys
import functools

def get_lines():
    return [line.rstrip('\n') for line in sys.stdin]

def numerize(string, splitBy=' '):
    return [int(item) for item in string.split(splitBy)]

def countZero(audience):
    return functools.reduce(lambda x, y: x + 1 if y[1] == 0 else x, audience, 0)

def countPerson(audience):
    return functools.reduce(lambda x, y: x + y[1], audience, 0)

lines = get_lines()
nbCases = numerize(lines.pop(0))[0]

for case in range(0, nbCases):
    infos = lines.pop(0).split(' ')
    neededFriends, totalPerson = 0, 0
    for shyLevel, nbPerson in enumerate(infos[1]):
        nbPerson = int(nbPerson)
        if shyLevel == 0 and nbPerson == 0:
            neededFriends += 1
            totalPerson += 1
        elif totalPerson < shyLevel:
            neededFriends += (shyLevel - totalPerson)
            totalPerson += (shyLevel - totalPerson)
        totalPerson += nbPerson
    print("Case #", (case + 1), ": ", neededFriends, sep="")
