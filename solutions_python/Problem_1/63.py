inputFileName = "A-large.in"
outputFileName = "A-large.out"

def solveCase(fileIn) :
    S = int(fileIn.readline())
    engines = [fileIn.readline()[:-1] for i in range(S)]
    Q = int(fileIn.readline())
    queries = [fileIn.readline()[:-1] for i in range(Q)]
    counter = 0
    l = engines[:]
    for query in queries :
        if l.count(query) :
            l.remove(query)
        if not l :
            l = engines[:]
            l.remove(query)
            counter += 1
    return counter

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
        fileOut.write(str(solveCase(fileIn)))
        fileOut.write("\n")
    fileIn.close()
    if outputFileName != "stdout":
        fileOut.close()

if __name__== "__main__" :
    main()
