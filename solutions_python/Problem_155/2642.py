__author__ = 't.town2'


def shyness(shy, maxShy):
    maxShy = int(maxShy)

    i = 1  # level of shyness currently at.
    level = int(shy[0])  # number of people standing
    extrasNeeded = 0
    while i <= maxShy:
        extra = max((i - level), 0)
        extrasNeeded += extra
        level += extra + int(shy[i])
        i += 1
    return extrasNeeded






f = open('standingOvation.in', 'r')
f2 = open('standingOvation.out', 'w')
f2.truncate(0)
nrCases = f.readline()
print(nrCases)

for i in range(0, int(nrCases)):
    print i
    shy = f.readline().strip("\n").split(" ")
    maxShy = shy[0]
    shy = shy[1]

    result = shyness(shy, maxShy)
    out = "Case #" + str(i+1) + ": " + str(result)
    out += "\n"
    f2.write(out)
