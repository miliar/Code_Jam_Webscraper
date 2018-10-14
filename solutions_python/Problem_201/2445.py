
def main(input):
    file = open(input)
    txt = file.read().split()
    file.close()


    file = open("result.txt", 'w')
    i = 0
    j = 1
    while i < int(txt[0])*2:
        spaces = int(txt[i+1])
        population = int(txt[i+2])
        #print spaces, population

        stalls = [1]
        for k in range(spaces):
            stalls.append(0)
        stalls.append(1)
        #print sidesSpaces(stalls, 3)

        if (population == spaces): file.write("Case #"+str(j)+": "+str("0 0")+"\n")
        #elif (population == 1): file.write("Case #"+str(j)+": "+str(spaces/2)+" "+str(spaces/2 - 1)+"\n")
        else:
            for p in range(population):
                result = fillPosition(stalls)
            file.write("Case #" + str(j) + ": " +str(result[2])+" "+str(result[0])+ "\n")
        j += 1
        i += 2
    file.close()

def sidesSpaces(stalls, index):

    left = right = 0

    i = index
    while i > 1 and stalls[i-1] == 0:
        left += 1
        i -= 1
    i = index
    while i < len(stalls)-2 and stalls[i+1] == 0:
        right += 1
        i += 1
    return left, right

def fillPosition(stalls):
    valuesFirst = []
    candidats = []
    candidatsSecond = []
    for i in range(1, len(stalls)-1):
        if stalls[i] == 0:
            distances = sidesSpaces(stalls, i)
            minDistance = min(distances[0], distances[1])
            maxDistance = max(distances[0], distances[1])
            valuesFirst.append((minDistance, i, maxDistance))
    valuesFirst.sort(key=lambda x: x[0], reverse=True)
    #print values
    maximum = valuesFirst[0][0]
    j = 0
    while j < len(valuesFirst) and valuesFirst[j][0] == maximum:
        candidats.append(valuesFirst[j])
        j += 1

    if len(candidats) == 1:
        stalls[candidats[0][1]] = 1
        return candidats[0]
    else:
        candidats.sort(key=lambda x: x[2], reverse=True)
        maximum = candidats[0][2]
        j = 0
        while j < len(candidats) and candidats[j][2] == maximum:
            candidatsSecond.append(candidats[j])
            j += 1
        if len(candidatsSecond) == 1:
            stalls[candidatsSecond[0][1]] = 1
            return candidatsSecond[0]
        else:
            candidatsSecond.sort(key=lambda x: x[1], reverse=False)
            stalls[candidatsSecond[0][1]] = 1
            return candidatsSecond[0]



main("C-small-1-attempt1.in")