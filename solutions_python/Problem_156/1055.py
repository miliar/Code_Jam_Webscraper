import sys
from collections import Counter

cost = lambda x, y: int(x/y) if x % y != 0 else int(x / y) - 1

def resolve(plates):
    occurs = sorted(Counter(plates).items(), key=lambda x: -x[0])
    currMin = occurs[0][0]
    for portion in range(1, currMin + 1):
        currCost = portion
        for x, occur in occurs:
            if x <= portion or currMin < currCost:
                break
            currCost += occur * cost(x, portion)
        currMin = min(currMin, currCost)
    return currMin

with open(sys.argv[1], 'r') as f:
    for i in range(int(f.readline())):
        f.readline()
        plates = map(lambda x: int(x), f.readline().split())
        print("Case #" + str(i + 1) + ": " + str(resolve(list(plates))))

