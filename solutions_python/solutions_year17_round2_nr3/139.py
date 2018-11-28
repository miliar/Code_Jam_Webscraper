# There's a stupid answer to the small case, we'll do that first

inputF = open('C-small-attempt0.in', 'r')
output = open('C-small-attempt0.out', 'w')


def startToEndTime(cityHorses, dists):
    # opt(i, j) = best time to finish in city j with horse i
    opt = [[10e12]*len(cityHorses) for i in range(len(cityHorses))]
    numCities = numHorses = len(cityHorses)
    # Initialize the first row:
    opt[0][0] = 0
    for i in range(1, numCities):
        #print dists[0:i]
        #print cityHorses[0][1]
        if sum(dists[0:i]) > cityHorses[0][1]:
            break
        else:
            opt[0][i] = sum(dists[0:i])*1.0/cityHorses[0][0]

    for i in range(1, numHorses):
        bestTimeToCityI = min([opt[k][i] for k in range(numHorses)])
        #print i, bestTimeToCityI
        for j in range(i+1, numCities):
            if sum(dists[i:j]) > cityHorses[i][1]:
                continue
            else:
                opt[i][j] = bestTimeToCityI + sum(dists[i:j])*1.0/cityHorses[i][0]

    return min([opt[k][-1] for k in range(numHorses)])


numCases = int(inputF.readline())

for i in range(numCases):
    n, q = inputF.readline().split()
    cityHorses = [] # list of (speed, distance)
    for j in range(int(n)):
        e, s = inputF.readline().split()
        cityHorses += [(int(s), int(e))]
    ds = []
    for j in range(1, int(n)):
        d = inputF.readline().split()[j]
        ds += [int(d)]
    inputF.readline()
    inputF.readline() # for small set, can ignore this

    t = startToEndTime(cityHorses, ds)
        
    output.write('Case #' + str(i+1) + ': ' + str(t) + '\n')
    
            
inputF.close()
output.close()
