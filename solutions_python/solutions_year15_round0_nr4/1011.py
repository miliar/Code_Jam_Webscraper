import sys

input = open(sys.argv[1])
numOfTests = int(input.readline())


ricLoseCases_X3 = [(2,3), (3,3), (3,4)]
ricLoseCases_X4 = [(3,4), (4,4)]

counter = 1

def checkIfRicWins(row):
    xStr, rStr, cStr = row.strip().split(" ")
    x = int(xStr)
    r = int(rStr)
    c = int(cStr)

    if x == 1:
        return False
    
    if x == 2 and ((r * c) % 2) == 0:
        return False

    matTuple = (min(r,c), max(r,c))
    if x == 3 and matTuple in ricLoseCases_X3:
            return False
    if x == 4 and matTuple in ricLoseCases_X4:
            return False

    return True

            
    
#only works for small input
for row in input:
    print "Case #" + str(counter) + ": " + ("RICHARD" if checkIfRicWins(row) else "GABRIEL")
    counter += 1
        
        
