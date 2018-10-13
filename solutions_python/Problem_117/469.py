#! /usr/bin/pypy

#the field is a matrix of ints now
def solve(N,M,field):
    #maximum of each row
    mRows = [max(field[row]) for row in range(N)]
    #maximum of each column
    mCols = [0 for col in range(M)]
    for row in range(N):
        for col in range(M):
            mCols[col] = max(field[row][col], mCols[col])

    #for each field entry
    for row in range(N):
        for col in range(M):
            if field[row][col] >= min(mCols[col],mRows[row]):
                continue
            else:
                return "NO"
    return "YES"


def processFile(filename):
    f = open(filename, "r")
    resultFile = open("result.txt","w")

    T = int(f.readline()) #number of cases
    print "Solving %s cases:"%(T,)

    solutions = []
    for case in range(T):
        (N,M) =  map(int,f.readline().split(" ")) #split one line, convert to int
        field = []
        for i in range(N):
            field.append(map(int,f.readline().strip().split(" ")))
        a = "Case #%s: %s"%(case+1,solve(N,M,field)) #solution line
        solutions.append(a)
        print a

    resultFile.write("\n".join(map(str,solutions)))

    resultFile.close()
    f.close()

if __name__ == "__main__":
    # something which needs to be precomputed goes here

    while True:
        print "Input filename to solve:"
        fileNameToSolve = raw_input()
        processFile(fileNameToSolve)

        print "Results have been written to result.txt"
