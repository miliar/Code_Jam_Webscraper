
INPUT = "D-small-attempt0.in"
OUTPUT = "D-small-attempt0.out"

def solve(X,R,C):
    if (X == 1):
        return "GABRIEL"
    if (X == 2):
        if ((R*C % 2) == 0):
            return "GABRIEL"
        else:
            return "RICHARD"
    if (X == 3):
        if (R*C == 6):
            return "GABRIEL"
        if (R*C<=8 or R*C==16): # small table
            return "RICHARD"
        return "GABRIEL"
    if (X == 4):
        if (R*C < 12):
            return "RICHARD"
        else:
            return "GABRIEL"

if __name__=="__main__":
    f_in = open(INPUT)
    f_out = open(OUTPUT,"w")
    lines = f_in.readlines()
    output = []
    cases = int(lines[0].strip())
    for i,line in enumerate(lines[1:]):
        data = line.strip().split(" ")
        X,R,C = int(data[0]), int(data[1]), int(data[2])
        output += "Case #%d: %s\n" % (i+1,solve(X,R,C))
        print i
        
    f_out.writelines(output)
    f_out.close()
    f_in.close()
    print 'done.'

