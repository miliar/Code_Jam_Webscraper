


def main(input):

    file = open(input)
    txt = file.read().split()
    file.close()

    t = int(txt[0])

    file = open("result.txt", 'w')

    i = 1
    j = 1
    while (i < t*2):
        results = []
        pancakes = list(txt[i])
        k = int(txt[i+1])
        #print pancakes, k
        tryFlip(pancakes, k, results)
        results.sort()
        if (len(results) > 0): file.write("Case #"+str(j)+": "+str(results[0])+"\n")
        else: file.write("Case #"+str(j)+": IMPOSSIBLE\n")
        i += 2
        j += 1

    file.close()

def tryFlip(pancakes, k, results):

    groups = calculateTotalGroups(len(pancakes), k)
    #print groups
    flipsMade = []

    return reverseGroup(pancakes, groups, 0, k, flipsMade, results)


def reverseGroup(pancakes, groups, it, k, flipsMade, results):

    if checkSolution(pancakes):
        results.append(it)
        return it

    #elif pancakes in flipsMade: return False, -1

    #elif len(groups) == 0: return -1

    else:
        copyList = list(pancakes)
        for i in range(groups):
            for j in range(k):
                if copyList[i+j] == '+': copyList[i+j] = '-'
                else: copyList[i+j] = '+'
            if copyList in flipsMade: return -1
            #newGroups = list(groups)
            #newGroups.remove(i)
            flipsMade.append(copyList)
            steps = reverseGroup(copyList, groups, it+1, k, flipsMade, results)
            flipsMade.remove(copyList)
            if steps != -1:
                results.append(steps)
                #return steps
            copyList = list(pancakes)
        return -1




def checkSolution(list):
    same = True
    i = 0
    while same and i < len(list):
        same = list[i] == '+'
        i += 1

    return same

def calculateTotalGroups(total, k):
    count = 0
    for i in range(total):
        if i+k <= total: count += 1
    return count

main("A-small-attempt2.in")
