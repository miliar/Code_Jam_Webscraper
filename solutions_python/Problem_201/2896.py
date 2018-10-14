import math
import bisect

results = []
lines = []
with open('test.in') as f:
    for line in f:
        lines.append(line.strip())
lines.pop(0)

for index, line in enumerate(lines):
    (number_of_stalls, number_of_people) = line.split(' ')
    number_of_stalls = int(number_of_stalls)
    number_of_people = int(number_of_people)
    indexTrue = [0, number_of_stalls + 1]

    minS = len(indexTrue)
    maxS = 0

    for x in range(number_of_people):
        bestIndex = -1
        bestDist = -1
        for y in range(len(indexTrue) - 1):
            dist = indexTrue[y + 1] - indexTrue[y]
            if dist > bestDist:
                bestDist = dist
                bestIndex = math.floor((dist / 2) + indexTrue[y])
        if x == (number_of_people - 1):
            indexInsert = (bisect.bisect_left(indexTrue, bestIndex))
            Ls = (bestIndex - indexTrue[indexInsert - 1]) - 1
            Rs = (indexTrue[indexInsert] - bestIndex) - 1
            minS = min(Ls, Rs)
            maxS = max(Ls, Rs)
        bisect.insort(indexTrue, bestIndex)
    results.append("Case #" + str(index + 1) + ": " + str(maxS) + " " + str(minS))

with open('res.txt', 'w') as f:
    for x in results:
        f.write(x + "\n")




