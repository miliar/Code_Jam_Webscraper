from __future__ import print_function
import sys
import math

def solveProblem(initialState):
    cakes = [( math.pi * r * 2 * h + math.pi * r * r, math.pi * r * 2 * h,  math.pi * r * r , r, h) for r, h in initialState["cakes"]]
    maxRadius = 0
    cakes.sort(None,None,True)
    k = initialState["k"]
    verticalArea = 0
    #pick the biggest one
    while not k == 0:
        cakes = [(ha + (max((math.pi * r * r) - (math.pi * maxRadius * maxRadius), 0)), ha, ta, r, h) for
                 toa, ha, ta, r, h in cakes]
        cakes.sort(None, None, True)
        thisCake = cakes.pop(0)
        k -= 1
        if thisCake[3] > maxRadius:
            maxRadius = thisCake[3]
        verticalArea += thisCake[1]
    total = math.pi * maxRadius * maxRadius + verticalArea
    print(total)
    return [str(total)], []

def main():
    inPath = sys.argv[1]
    outPath = inPath.split('.')[0] + '.out'
    file = open(inPath, "r")
    out = open(outPath, "w")
    #Read number of cases
    cases = int(file.readline())
    #Problem specific state definitions
    initialState = {}
    for i in range(1, cases + 1):
        #Case input
        caseDef = file.readline()
        values = caseDef.split(" ")
        initialState["n"] = int(values[0])
        initialState["k"] = int(values[1])
        initialState["cakes"] = []
        for j in range(initialState["n"]):
            defLine = file.readline()
            defLine = defLine.split(" ")
            initialState["cakes"].append((int(defLine[0]), int(defLine[1])))
        print("Solving Case: " + str(i))
        header, results = solveProblem(initialState)
        #format header
        headerStr = " ".join(header)
        print('Case #{case}: {headerStr}'.format(case=i, headerStr=headerStr), file=out)
        #format the rest of the results
        for result in results:
            print(' '.join(result), file=out)

if __name__ == "__main__":
    main()