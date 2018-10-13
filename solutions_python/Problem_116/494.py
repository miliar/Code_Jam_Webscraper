#! /usr/bin/pypy

def check(c0,c1,c2,c3):
    d = {"X":0,"O":0,"T":0,".":0}
    d[c0]+=1
    d[c1]+=1
    d[c2]+=1
    d[c3]+=1

    if d["O"] == 4 or (d["T"] == 1 and d["O"] == 3):
        return [True,"O won"]
    if d["X"] == 4 or (d["T"] == 1 and d["X"] == 3):
        return [True,"X won"]

    return [False, d["."] != 0]

def solve(field):
    freeFieldFlag = False #if there was a field free

    #check rows
    for line in field:
        sol = check(line[0],line[1],line[2],line[3])
        if sol[0]:
            return sol[1]
        freeFieldFlag = sol[1] or freeFieldFlag

    #check rows
    for i in range(4):
        sol = check(field[0][i],field[1][i],field[2][i],field[3][i])
        if sol[0]:
            return sol[1]
        freeFieldFlag = sol[1] or freeFieldFlag

    #check diagonals
    sol = check(field[0][0],field[1][1],field[2][2],field[3][3])
    if sol[0]:
        return sol[1]
    freeFieldFlag = sol[1] or freeFieldFlag
    sol = check(field[0][3],field[1][2],field[2][1],field[3][0])
    if sol[0]:
        return sol[1]
    freeFieldFlag = sol[1] or freeFieldFlag

    if freeFieldFlag:
        return "Game has not completed"
    return "Draw"

def processFile(filename):
    f = open(filename, "r")
    resultFile = open("result.txt","w")

    T = int(f.readline()) #number of cases
    print "Solving %s cases:"%(T,)

    #read the other lines
    solutions = []
    lines = f.readlines()
    for i in range(T):
        #4x4 playing field - list of strings
        field = [lines[i*5+x].strip() for x in range(4)]

        a = "Case #%s: %s"%(i+1,solve(field))
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
