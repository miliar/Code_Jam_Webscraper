f = open("B-small-attempt1.in", "r")
#f = open("A-large.in", "r")
#f = open("input2.txt", "r")
num_cases = int(f.readline())
cases = []
import sys
sys.setrecursionlimit(2000)
for c in range(num_cases):
    cases.append((f.readline(), f.readline()))
    
def processCase(case):
    numPlates = int(case[0])
    tok = case[1].split()
    #print tok
    pancakes = [int(x) for x in tok]
    return [numPlates, pancakes]

def processTest(test):
    numPancakes = sum(test[1])
    return timeEat(test[0], test[1])
def timeEat(plates, panArray):
    if sum(panArray) <= 0:
        return 0
    if max(panArray) == 1:
        return 1
    if max(panArray) == 2:
        return 2
    if max(panArray) == 3:
        return 3
    #next = [(lambda x: x-1 if x >0 else 0)(x) for x in panArray]
    next = [x-1 for x in panArray if x-1 > 0]
    
    nextPlates = len(next)
    special = panArray[:]
    special2 = panArray[:]
    special3 = panArray[:]
    pmax = max(panArray)
    pindex = panArray.index(pmax)
    """
    for x in range(plates):
        if panArray[x] > pmax:
            pmax = panArray[x]
            index = x
    """
    
    if panArray[pindex] % 2 == 0:
        special.append(special[pindex]/2)
        special[pindex] = special[pindex]/2
            
        if max >=4:
            special2.append(special2[pindex]/2+1)
            special2[pindex] = special2[pindex]/2-1
        else:
            special2.append(0)
        if max >= 6:
            special3.append(special3[pindex]/2+2)
            special3[pindex] = special3[pindex]/2-2
        else:
            special3.append(0)
    else:
        special.append(special[pindex]/2)
        special[pindex] = special[pindex]/2 + 1
        if max >=5:
            special2.append(special2[pindex]/2-1)
            special2[pindex] = special2[pindex]/2+2
        else:
            special2.append(0)
        if max >= 7:
            special3.append(special3[pindex]/2-2)
            special3[pindex] = special3[pindex]/2+3    
        else:
            special3.append(0)



    
    if pmax != 1:
        v1 = 1+timeEat(nextPlates, next)
        v2 = 1+timeEat(plates+1, special)
        v3 = 1+timeEat(plates+1, special2)
        #v4 = 1+timeEat(plates+1, special3)
        #print panArray
        #print v1, v2,
        return min(v1, v2, v3)
    else:
        return 1
cnum = 1
g = open("2-out.txt", "w")
for c in cases:
    print processCase(c)
    value = processTest(processCase(c))
    print("Case #{}: {}".format(cnum, value))
    g.write("Case #{}: {}\n".format(cnum, value))
    cnum+=1