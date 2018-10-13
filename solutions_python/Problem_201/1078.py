from math import ceil, floor
from bisect import insort
from operator import itemgetter

with open("C-small-2-attempt1.in") as f:
    s = f.read().splitlines()

def solve(n,k):
    stalls = {str(n):1}
    seed = [n]
    while len(seed) > 0:
        currVal = seed[-1]
        
        numToAdd = stalls[str(currVal)]
        if currVal %2 == 0:
            val1 = int(currVal/2)
            val2 = val1 - 1
        else:
            val1 = int(floor(currVal/2))
            val2 = val1
        if str(val1) in stalls:
            stalls[str(val1)] += numToAdd
        else:
            stalls[str(val1)] = numToAdd
        if str(val2) in stalls:
            stalls[str(val2)] += numToAdd
        else:
            stalls[str(val2)] = numToAdd
        if val1 > 0 and seed[0] != val1:
            insort(seed,val1)
        if val2 > 0 and seed[0] != val2:
            insort(seed,val2)
        seed = seed[:-1]
    itemList = [[int(item[0]),item[1]] for item in stalls.items()]
    itemList.sort(key=itemgetter(0),reverse=True)
    for entry in itemList:
        if entry[1] >= k:
            if entry[0] % 2 == 0:
                if entry[0] == 0:
                    return [0,0]
                else:
                    return [int(entry[0]/2),int(entry[0]/2)-1]
            else:
                return [int(floor(entry[0]/2))]*2
        k -= entry[1]

with open("output.txt","a") as f:
    counter = 1
    for line in s[1:]:
        n, k = line.split(" ")
        n = int(n)
        k = int(k)
        out = solve(n,k)
        f.write("Case #"+str(counter)+": "+str(out[0])+" "+str(out[1])+"\n")
        counter += 1
    

