from math import ceil, floor

def readFile(inFile, outFile):
    with open(inFile) as f:
        line1 = f.readline()
        #print("Number of Cases: ", line1)
        counter = 1
        for line in f:
            line = line.strip()
            calculateSolution(line, counter, outFile)
            counter += 1

def calculateSolution(line, counter, outFile):
    global erg
    erg = list()
    h = line.split()
    stalls = int(h[0])
    customers = int(h[1])
    doSolve(stalls, customers, 0)
    solution = erg[customers-1]
    maxS = max(solution)
    minS = min(solution)
    #print(line)
    #print("Solution : " + str(maxS) + " , " + str(minS) + "\n")
    with open(outFile, 'a') as f:
        f.write("Case #%i: %i %i\n"  %(counter,maxS, minS))
    
def solve(stalls, customers):
    while customers > 1:
        stalls = stalls // 2
        customers = customers - 2 # oder // 2
    stalls = stalls - customers
    if stalls % 2 == 0:
        return stalls/2, stalls/2-1
    else:
        return (stalls-1)/2, (stalls-1)/2
        
def doSolve(stalls, customers, depth):
    if (2**depth > customers):
        return
    if stalls % 2 == 0:
        x = (stalls // 2) - 1
        y = stalls // 2
    else:
        x = (stalls - 1) // 2
        y = (stalls - 1) // 2
    insertInMyTulple(x, y)
    doSolve(x, customers, depth+1)
    doSolve(y, customers, depth+1)
    
    
def insertInMyTulple(x, y):
    global erg
    if erg == list():
        erg = [(x, y)]
    else:
        for i in range(len(erg)):
            u, v = erg[i]
            if (x+y) > (u+v):
                erg = erg[:i] + [(x,y)] + erg[i:]
                return
        erg += [(x, y)]
    
erg = list()
readFile("C-small-1-attempt4.in", "C-small-1-attempt4.out")
