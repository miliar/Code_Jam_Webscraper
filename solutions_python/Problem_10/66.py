inputFileName = "A-large.in"
outputFileName = "A-large.out"

def solve(P, K, L, frequencies) :
    keys = [[] for i in range(K)]
    frequencies = list(reversed(sorted(frequencies)))
    k = 0
    for f in frequencies :
        keys[k] += [f]
        if len(keys[k]) > P+1 :
            return False
        k = (k + 1) % K
    s = 0
    for key in keys :
        for i in range(len(key)) :
            s += key[i]*(i+1)
    return s
    

def solveCase(fileIn) :
    P, K, L = [int(x) for x in fileIn.readline().split()]
    frequencies = [int(x) for x in fileIn.readline().split()]
    return str(solve(P, K, L, frequencies))

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
