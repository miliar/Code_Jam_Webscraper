import collections, sys, os, math

def locate_max(a):
    biggest = max(a)
    return biggest, [index for index, element in enumerate(a)
                      if biggest == element]

def locate_min(a):
    smallest = min(a)
    return smallest, [index for index, element in enumerate(a)
                      if smallest == element]


def solve_test_case(N,K):
    if K == N:
        return (0,0)
    else:
        sets = list([N])
        i = 0
        while i < K:
            sizeSubset, indicesSubsets = locate_max(sets)
            indexSubset = indicesSubsets[0]
            subst = []
            numberEquals = len(indicesSubsets)
            if sizeSubset == 2:
                #sets[indexSubset] = 1
                if K <= i + numberEquals:
                    return (1,0)
                else:
                    return (0,0)#sets[indexSubset] = 1
            elif K <= i + numberEquals:
                if sizeSubset %2 == 0:
                    return (int(sizeSubset /2), (int(sizeSubset/2) - 1))
                else:
                    return (math.floor(sizeSubset/2), math.floor(sizeSubset/2))
            elif sizeSubset % 2 == 0:
                subst = [int(sizeSubset / 2 - 1), int(sizeSubset /2)]
            else:
                subst = [math.floor(sizeSubset/2),math.floor(sizeSubset/2)]
            tmpSet = []
            for j,indexSubset in enumerate(indicesSubsets):
                if j == 0:
                    tmpSet = sets[0:indexSubset]
                for sub in subst:
                    tmpSet.append(sub)
                if j < (len(indicesSubsets) - 1):
                    for rest in sets[(indexSubset+1):(indicesSubsets[j+1])]:
                        tmpSet.append(rest)
                else:
                    for rest in sets[(indexSubset+1):]:
                        tmpSet.append(rest)
            sets = tmpSet
            #print(sets)
            i = i + numberEquals
            #print(sets)
        sizeSubset, indicesSubsets = locate_max(sets)
        #Pick stall
        if sizeSubset == 2:
            return (1,0)
        elif sizeSubset %2 == 0:
            return (int(sizeSubset /2), (int(sizeSubset/2) - 1))
        else:
            return (math.floor(sizeSubset/2), math.floor(sizeSubset/2))

testCases = []

inputFilename = sys.argv[1]
outputFilename = os.path.splitext(inputFilename)[0] + '.out'

with open(inputFilename,'r') as f:
    next(f)
    for line in f:
        testCases.append(list(map(int, [n for n in line.rstrip().split()])))


solutions = [solve_test_case(TC[0],TC[1]) for TC in testCases]
for i,sol in enumerate(solutions):
    print("Case #%d: %d %d" % ((i+1),sol[0], sol[1]))
