infile = open("D-small-attempt1.in","r")
outfile = open("D-small-attempt1.out","w")

def solve(X, R, C):
    if (R*C)%X != 0:
        return "RICHARD"
    if X == 1:
        return "GABRIEL"
    if X == 2:
        return "GABRIEL"
    if X == 3:
        if R%3 == 0:
            if C > 1:
                return "GABRIEL"
        elif C%3 == 0:
            if R > 1:
                return "GABRIEL"
        return "RICHARD"
    if X == 4:
        if R%4 == 0:
            if C > 2:
                return "GABRIEL"
        elif C%4 == 0:
            if R > 2:
                return "GABRIEL"
        return "RICHARD"
T = int(infile.readline())
for case in range(T):
    solution = ""
    X, R, C = map(int, infile.readline().split())
    solution = solve(X, R, C)
    outfile.write("Case #" + str(case+1) + ": " + solution + "\n")

infile.close()
outfile.close()
