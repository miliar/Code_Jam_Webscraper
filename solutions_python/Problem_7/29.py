inFile = open("A-small-attempt0.in", "r")
outFile = open("A-small-out.out", "w")

cases = int(inFile.readline())

for caseNum in range(cases):

    parameters = inFile.readline().split(" ")
    parameters = map(int, parameters)
##    print parameters

    n = parameters[0]
    A = parameters[1]
    B = parameters[2]
    C = parameters[3]
    D = parameters[4]
    Xi = parameters[5]
    Yi = parameters[6]
    M = parameters[7]

    trees = [(Xi, Yi)]
    
    X = Xi
    Y = Yi

    
    for i in range(1, n):
        X = (A * X + B) % M
        Y = (C * Y + D) % M
        treeTuple = (X, Y)
        trees.append(treeTuple)

    ##print trees
    count = 0

    for i in range(0, n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                ##print trees[i], trees[j], trees[k]
                xGrid = trees[i][0] + trees[j][0] + trees[k][0]
                yGrid = trees[i][1] + trees[j][1] + trees[k][1]
                ##print xGrid, yGrid
                if (trees[i][0] + trees[j][0] + trees[k][0]) % 3 == 0 and (trees[i][1] + trees[j][1] + trees[k][1]) % 3 == 0:
                    count = count + 1
    
    ##print count

    outputString = "Case #" + str(caseNum + 1) + ": " + str(count) + "\n"
    print outputString.rstrip()

    outFile.write(outputString)




inFile.close()
outFile.close()
