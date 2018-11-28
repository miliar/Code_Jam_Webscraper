inputFileName = "A-small-attempt0.in"
outputFileName = "A-small-attempt0.out"

def solve(trees):
    T = len(trees)
    counter = 0
    for i in range(T) :
        p1 = trees[i]
        for j in range(i+1, T) :
            p2 = trees[j]
            for k in range(j+1, T) :
                p3 = trees[k]
                if (p1[0]+p2[0]+p3[0]) % 3 == 0 and (p1[1]+p2[1]+p3[1]) % 3 == 0 :
                    counter += 1
    return counter

def solveCase(fileIn) :
    n, A, B, C, D, x0, y0, M = [int(x) for x in fileIn.readline().split()]
    X = x0; Y = y0
    trees = [(X, Y)]
    for i in range(n-1) :
        X = (A * X + B) % M
        Y = (C * Y + D) % M
        trees += [(X, Y)]
    return str(solve(trees))

def main() :
    import sys
    fileIn = open(inputFileName)
    if outputFileName == "stdout" :
        fileOut = sys.stdout
    else :
        fileOut = open(outputFileName, "w")
    N = int(fileIn.readline())
    for i in range(N) :
        fileOut.write("Case #%d: " % (i+1))
        fileOut.write(solveCase(fileIn))
        fileOut.write("\n")
    fileIn.close()
    if outputFileName != "stdout":
        fileOut.close()

if __name__== "__main__" :
    main()
