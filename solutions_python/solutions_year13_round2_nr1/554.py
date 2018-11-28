#! /usr/bin/pypy

#own size, count others, other sizes
def solve(A,N,s):
    s.sort()
    idx = 0
    ops = 0
    ops_pending = 0

    motes_left = len(s)

    while idx < len(s):
        if s[idx] < A:
            ops += ops_pending
            ops_pending = 0

            A+=s[idx]
            idx+=1
            motes_left-=1
        else:
            A+=A-1
            ops_pending+=1

            if motes_left == ops_pending:
                ops += ops_pending
                break

    return ops

def processFile(filename):
    f = open(filename, "r")
    resultFile = open("result.txt","w")

    T = int(f.readline()) #number of cases in the first line
    print "Solving %s cases:"%(T,)

    #read the other lines
    solutions = []
    for i in range(T):
        A, N = map(int,f.readline().split(" "))
        s =  map(int,f.readline().split(" "))

        a = "Case #%s: %s"%(i+1, solve(A,N,s)) #solution line
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
