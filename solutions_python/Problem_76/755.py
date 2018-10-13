def PlaceItem(sits, item):
    result = []
    for sit in sits:
        result += [[sit[0] + item, sit[1], sit[2] ^ item, sit[3]]]
        result += [[sit[0], sit[1] + item, sit[2], sit[3] ^ item]]
    return result

def ShareCandy(candies):
    result = [[0, 0, 0, 0]]
    for candy in candies:
        result = PlaceItem(result, candy)
    return result

def Determine(candies):
    share = ShareCandy(candies)
    best = 0
    for i in share:
        if i[2] == i[3] and i[0] > best and i[0] != 0 and i[1] != 0:
            best = i[0]
    if best == 0:
        return "NO"
    return str(best)

fin = file("candy.in")
lines = fin.readlines()
count = int(lines[0])
for i in range(count):
    print "Case #" + str(i + 1) + ": " + Determine([int(i) for i in lines[2 + 2 * i].split(" ")])
