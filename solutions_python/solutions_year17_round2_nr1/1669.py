from __future__ import print_function
import sys
import math

def solveProblem(initialState):
    print(initialState)
    result = []
    horses = initialState['horses']
    horses.sort()
    reverse = reversed(horses)
    d = initialState['d']
    lowestSpeed = float("inf")
    timeTaken = 0
    later = []
    for i in reverse:
        if lowestSpeed >= i[1]:
            lowestSpeed = i[1]
            later = [(0, float(d - i[0])/float(i[1]), i[0], i[1], i[1])]
        else:
            for j in range(len(later)):
                it, itt, id, prs, pos = later[j]
                if prs > i[1]:
                    pass
                else:
                    intersectTime = (float(id) - float(i[0]))/(float(i[1]) - float(prs))
                    intersectDist = i[0] + intersectTime * i[1]
                    intersectpostSpeed = pos
                    intersectpreSpeed = i[1]

                    if intersectTime > itt:
                        later[j] = (0, 0, id, prs, pos)
                        later.append((it, float(d - i[0])/float(i[1]), intersectDist, intersectpreSpeed, intersectpostSpeed))
                    else:
                        later[j] = (intersectTime, itt, id, prs, pos)
                        later.append((it, intersectTime, intersectDist, intersectpreSpeed, intersectpostSpeed))

    later.sort()
    print(later)
    totalTime = 0
    for l in later:
        totalTime += l[1] - l[0]
    speed = d/totalTime




    return [str(speed)], result



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
        D, N = caseDef.split(" ")
        initialState["n"] = int(N)
        initialState["d"] = int(D)
        initialState["horses"] = []
        for j in range(initialState["n"]):
            defLine = file.readline()
            defLine = defLine.split(" ")
            initialState["horses"].append((int(defLine[0]), int(defLine[1])))
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