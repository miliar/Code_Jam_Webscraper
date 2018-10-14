def parseFromFile(path):
    with open(path) as f:
        data = f.read()
    return parseInput(data)

def parseInput(inp):
    inp = inp.splitlines()[1:]
    text = []
    for i in range(len(inp)):
        l = inp[i].split()
        res = ("Case #%d: %f" % (i+1, tryBuy(*tuple(map(float, [l[0], l[1], l[2]])))))
        text.append(res)
        #print (res)

    with open("res.out", "w") as f:
        f.write("\n".join(text))

def tryBuy(farmCost, cookieRate, goal):
    currentRate = 2
    time = 0.0
    i = 0
    while True:
        if goal/currentRate < farmCost/currentRate + goal/(currentRate + cookieRate):
            # print ("Stop at %d" % i)
            break
        time += farmCost/currentRate
        currentRate += cookieRate
        # print ("Time cost: %d, currentRate: %d" % (farmCost/currentRate, currentRate))
        i += 1
    # print ("Before: %d" % time)
    time += goal/currentRate
    return time
