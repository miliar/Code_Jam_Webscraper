nb = int(raw_input())

for i in range(nb):
    data = raw_input().split(' ')
    maxShyness = int(data[0])
    distrib = data[1]
    currentShynessLevel = 0
    res = 0
    for (j,c) in enumerate(distrib):
        attended = int(c)
        if attended != 0 and j > currentShynessLevel:
            res += j - currentShynessLevel
            currentShynessLevel += j - currentShynessLevel
        currentShynessLevel += attended
    print "Case #{}: {}".format(i+1, res)
        