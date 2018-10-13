def getweights():
    weights = file.readline().split()
    for (a, b) in enumerate(weights):
        weights[a] = float(b)
    return weights

with open('D-large.in') as file:
    cases = int(file.readline())
    output = open('output.txt','w')
    for c in range(1, cases + 1):
        n = int(file.readline())
        naomi, ken = sorted(getweights()), sorted(getweights())
        deceit, war = 0, 0
        lowestken = 0
        for i in range(n):
            if naomi[i]>ken[lowestken]:
                deceit += 1
                lowestken += 1
        for i in range(n):
            w = 0
            while naomi[i]>ken[w]:
                w+=1
                if w == len(ken):
                    w = 0
                    break
            if ken.pop(w) < naomi[i]:
                war += 1
        output.write('Case #%d: %d %d\n' % (c, deceit, war))
