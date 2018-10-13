f = open("D-small-attempt0.in", "r")
#f = open("D-large.in", "r")
#f = open("input4.txt", "r")
num_cases = int(f.readline())
cases = []
for c in range(num_cases):
    cases.append(f.readline())
    
def processCase(case):
    tok = case.split()
    ominos = [int(x) for x in tok]
    return ominos
    
  
    
def processTest(test):
    N = test[0]
    R = test[1]
    C = test[2]
    if (R*C)%N != 0:
        return "RICHARD"
    if N == 1:
        return "GABRIEL"
    elif N == 2:
        if min(R, C) == 1 and max(R,C) == 1:
            return "RICHARD"
        if min(R, C) == 1 and max(R,C) == 2:
            return "GABRIEL"
        if min(R, C) == 1 and max(R,C) == 3:
            return "RICHARD"
        if min(R, C) == 1 and max(R,C) == 4:
            return "GABRIEL"
        if min(R, C) == 2 and max(R,C) == 2:
            return "GABRIEL"
        if min(R, C) == 2 and max(R,C) == 3:
            return "GABRIEL"
        if min(R, C) == 2 and max(R,C) == 4:
            return "GABRIEL"
        if min(R, C) == 3 and max(R,C) == 3:
            return "RICHARD"
        if min(R, C) == 3 and max(R,C) == 4:
            return "GABRIEL"
        if min(R, C) == 4 and max(R,C) == 4:
            return "GABRIEL"
    elif N == 3:
        if min(R, C) == 1 and max(R,C) == 1:
            return "RICHARD"
        if min(R, C) == 1 and max(R,C) == 2:
            return "RICHARD"
        if min(R, C) == 1 and max(R,C) == 3:
            return "RICHARD"
        if min(R, C) == 1 and max(R,C) == 4:
            return "RICHARD"
        if min(R, C) == 2 and max(R,C) == 2:
            return "RICHARD"
        if min(R, C) == 2 and max(R,C) == 3:
            return "GABRIEL"
        if min(R, C) == 2 and max(R,C) == 4:
            return "RICHARD"
        if min(R, C) == 3 and max(R,C) == 3:
            return "GABRIEL"
        if min(R, C) == 3 and max(R,C) == 4:
            return "GABRIEL"
        if min(R, C) == 4 and max(R,C) == 4:
            return "RICHARD"
    elif N == 4:
        if min(R,C) == 1:
            return 'RICHARD'
        if min(R, C) == 2 and max(R,C) == 2:
            return "RICHARD"
        if min(R, C) == 2 and max(R,C) == 3:
            return "RICHARD"
        if min(R, C) == 2 and max(R,C) == 4:
            return "RICHARD"
        if min(R, C) == 3 and max(R,C) == 3:
            return "RICHARD"
        if min(R, C) == 3 and max(R,C) == 4:
            return "GABRIEL"
        if min(R, C) == 4 and max(R,C) == 4:
            return "GABRIEL"
cnum = 1
g = open("D-out.txt", "w")
#g = open("D-large-out.txt", "w")
for c in cases:
    print processCase(c)
    value = processTest(processCase(c))
    print("Case #{}: {}".format(cnum, value))
    g.write("Case #{}: {}\n".format(cnum, value))
    cnum+=1