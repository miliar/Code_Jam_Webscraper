#! /usr/bin/pypy

def solve(r1, f1, r2, f2):
    candidates = f1[4*(r1-1):4*(r1-1)+4]
    new_candidates = f2[4*(r2-1):4*(r2-1)+4]

    count = 0
    the_number = 0
    for c in candidates:
        if c in new_candidates:
            count+=1
            the_number = c

    if count == 0:
        return "Volunteer cheated!"
    if count > 1:
        return "Bad magician!"
    return the_number

def processFile(filename):
    f = open(filename, "r")
    resultFile = open("result.txt","w")

    T = int(f.readline()) #number of cases in the first line
    print "Solving %s cases:"%(T,)

    #read the other lines
    solutions = []
    for s in range(T):
        r1 = int(f.readline())
        field1 = map(int, (" ".join(f.readline() for i in range(4))).split() )
        r2 = int(f.readline())
        field2 = map(int, (" ".join(f.readline() for i in range(4))).split() )

        a = "Case #%s: %s"%(s+1,solve(r1, field1, r2, field2))
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
