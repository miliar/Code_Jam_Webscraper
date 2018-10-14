def var(nums, n):
    tot = 0
    for i in nums:
        tot += abs(i - n)
    return tot

def best(nums):
    bestVar = None
    for n in nums:
        if bestVar == None or var(nums, n) < bestVar:
            bestVar = var(nums, n)
        if bestVar == 0:
            return 0
    return bestVar

def doit(lstrings):
    new = {}
    for string in lstrings:
        new[string] = string[0]
        for i in string:
            if i != new[string][-1]:
                new[string] += i

    new1 = new.values()[0]
    for i in new.values():
        if i != new1:
            return -1
    
    tick = {}
    for string in lstrings:
        for i in range(len(string)):
            if i == 0:
                tick[string] = [1]
            else:
                if string[i] == string[i-1]:
                    tick[string][-1] += 1
                else:
                    tick[string].append(1)


    value1 = tick.values()[0]                


    tock = [[] for i in range(len(value1))]
    for i in range(len(value1)):
        for j in tick.values():
            tock[i].append(j[i])


    res = 0
    for i in tock:
        res += best(i)

    return res


res = []
for i in range(input()):
    inpt = []
    for j in range(input()):
        inpt.append(raw_input())
    res.append(doit(inpt))

for i in range(len(res)):
    if res[i] != -1:
        print 'Case #' + str(i+1) + ': ' + str(res[i])
    else:
        print 'Case #' + str(i+1) + ': ' + 'Fegla Won'
