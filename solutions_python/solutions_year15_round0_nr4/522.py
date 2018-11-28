import math

def doCase(line):
    X = int(line[0])
    R = int(line[1])
    C = int(line[2])
    
    if (X > R and X > C):
        return "RICHARD"
    
    if (math.ceil(float(X) / 2) > R or math.ceil(float(X) / 2) > C):
        return "RICHARD"
    
    if (R * C % X > 0):
        return "RICHARD"
        
    if (X == 4 and R * C == 8):
        return "RICHARD"
        
    return "GABRIEL"

lines = [line.strip().split() for line in open('D-small-attempt3.in')]

out = open('output.txt', 'w')
for i in range(1, int(lines[0][0]) + 1):
    out.write("Case #" + str(i) + ": " + str(doCase(lines[i])) + "\n")
out.close