import string

FILENAME = "B-large.in"
inFile = open(FILENAME, 'r', 0)
fout = open("B_res.in", "w")
line = inFile.readline()
T = int(string.split(line)[0])

def maxcolumn(c, L):
    tempL = []
    for r in range(len(L)):
        tempL.insert(101, L[r][c])
    for i in range(len(tempL)):
        if tempL[i] == max(tempL):
            return i

for t in range(T):
    res = True
    L = []
    spec = inFile.readline()
    row = int(string.split(spec)[0])
    column = int(string.split(spec)[1])

    for r in range(row):
        line = string.split(inFile.readline())
        subL = []
        for i in range(len(line)):
            subL.insert(101, int(line[i]))
        L.insert(101, subL)

    diff = []
    for r in range(row):
        diff.insert(101,max(L[r]))
        
    for c in range(column):
        for r in range(row):
            if L[r][c] < diff[r]:
                if L[r][c] != L[maxcolumn(c, L)][c]:
                    res = False
        
    if res == False:
        fout.write ("Case #" + str(t+1) + ": NO\n")
    else:
        fout.write ("Case #" + str(t+1) + ": YES\n")
    
    
fout.close()
