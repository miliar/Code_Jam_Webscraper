import sys, copy;

def solve(r,c,m):
    emptyRows = []
    for i in range(0,r):
        currentColor = None
        for j in range(0,c):
            #print m[i][j]
            if m[i][j] != '?':
                currentColor = m[i][j]
            else:
                if currentColor != None:
                    m[i][j] = currentColor
        currentColor = None
        for j in range(0,c):
            #print m[i][j]
            if m[i][c-1-j] != '?':
                currentColor = m[i][c-1-j]
            else:
                if currentColor != None:
                    m[i][c-1-j] = currentColor
        if m[i][0] == '?':
            emptyRows.append(i)
            
    for i in range(1,r):
        if i in emptyRows and not i-1 in emptyRows:
            m[i] = m[i-1]
            emptyRows.remove(i)
    #print "m:",m
    #print "er:",emptyRows
    for i in range(1,r):
        #print "debug", i, r-1-i, r-i
        #print "debug",m[r-1-i], m[r-i]
        if r-1-i in emptyRows and not r-i in emptyRows:
            m[r-1-i] = m[r-i]
            emptyRows.remove(r-1-i)
            #print "debu ",m[r-1-i], m[r-i]
    #print [ "".join(m[i]) for i in range(0,r)]
    return "\n".join([ "".join(m[i]) for i in range(0,r)]);

inputFile =  sys.argv[1] if (len(sys.argv) > 1) else "input.txt";
outputFile = sys.argv[2] if (len(sys.argv) > 2) else (inputFile + "out.txt") if (len(sys.argv) > 1) else "output.txt";
print(inputFile, outputFile)
file = open(outputFile, "w")

with open(inputFile, 'r') as f:
    t = int(f.readline())
    print(t)
    for i in range(1, t + 1):
        file.write("Case #" + str(i) + ": \n")
        r,c = map(int, f.readline().split())
        m = [ list(f.readline().split('\n')[0]) for i in range(0,r) ]
        
            
        file.write(str(solve(r,c,m)) + "\n")
file.close()            








