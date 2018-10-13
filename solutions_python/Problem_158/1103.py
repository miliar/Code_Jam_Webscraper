def readFile(fname):
    f = open(fname)
    T = int(f.readline().strip())
    cases = []
    for line in f:
        cases.append([int(x) for x in line.strip().split()])

    return cases

def solve(case):
    X = case[0] # N-ominio size
    R = case[1] # grid parameter
    C = case[2] # grid parameter

##    if R == 1:
##        if X > 3:
##            return 'RICHARD'
##        elif C % X == 0:
##            return "GABRIEL"
##        else:
##            return "RICHARD"
##    elif C == 1:
##        if X > 3:
##            return 'RICHARD'
##        elif R % X == 0:
##            return "GABRIEL"
##        else:
##            return "RICHARD"
    if X > R and X > C:
        return "RICHARD"
    elif (R*C) % X != 0:
        return "RICHARD"
    elif X/2 > R or X/2 > C:
        return "RICHARD"
    elif (X > (2*R)) or (X > (2*C)):
        return "RICHARD"
    elif X == 4 and (R < 3 or C < 3):
        return "RICHARD"
    else:
        return "GABRIEL"

def main(fname):
    cases = readFile(fname)
    fout = open('outD.txt','w')
    for i in range(len(cases)):
        if i == 0: fout.write("Case #" + str(i+1) + ": " + solve(cases[i]))
        else: fout.write("\nCase #" + str(i+1) + ": " + solve(cases[i]))
    fout.close()

def test():
    cases = [[2,2,2],
             [2,1,3],
             [4,4,1],
             [3,2,3]]
    
    for i in range(len(cases)):
        print "Case #" + str(i+1) + ": " + solve(cases[i])
    
