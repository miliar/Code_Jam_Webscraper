import math
T = int(raw_input().strip())
for i in range(T):
#    print "case #: ", i+1

    temp = map(int, raw_input().strip().split(" "))
    R = temp[0] # number of rows
    C = temp[1] # number of columns
#    print "R = ", R
#    print "C = ", C
    cake = []
    newCake = []
    for j in range(R):
        cake.append(raw_input().strip())
        newCake.append("")

#    print cake
    

    firstRealRow = R
    for j in range(R):
        if cake[j] != "?" * C: # i.e. if row is not empty
            start = 0
            for k in range(C):
                if cake[j][k] != "?":
                    newLetter = cake[j][k]
                    newCake[j] += newLetter * (k-start+1)
                    start = k+1
                elif k == C-1: # at the end of a row
                    newCake[j] += newLetter * (k-start+1)
            if firstRealRow == R:
                firstRealRow = j
        else:
            newCake[j] = "?" * C
    
    
    
    for j in range(R):
        if j< firstRealRow:
            newCake[j] = newCake[firstRealRow][:]
        elif newCake[j] == "?" * C:
            newCake[j] = newCake[j-1][:]
    
#    print newCake



        
    print "case #" + str(i+1) + ":" # " + str(answer)
    for j in range(R):
        print newCake[j]


