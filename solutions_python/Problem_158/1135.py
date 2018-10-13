def OminousOmino(X, R, C):
    if X == 1:
        return "GABRIEL"
    if X == 2:
        if R % 2 == 0 or C % 2 == 0:
            return "GABRIEL"
        else:
            return "RICHARD"
    if X == 3:
        if (R % 3 == 0 or C % 3 == 0) and R > 1 and C > 1:
            return "GABRIEL"
        else:
            return "RICHARD"
    if X == 4:
        if R == 1 and C == 1:
            return "RICHARD"
        if R == 1 and C == 2:
            return "RICHARD"
        if R == 1 and C == 3:
            return "RICHARD"
        if R == 1 and C == 4:
            return "RICHARD"
        if R == 2 and C == 1:
            return "RICHARD"
        if R == 2 and C == 2:
            return "RICHARD"
        if R == 2 and C == 3:
            return "RICHARD"
        if R == 2 and C == 4:
            return "RICHARD"
        if R == 3 and C == 1:
            return "RICHARD"
        if R == 3 and C == 2:
            return "RICHARD"
        if R == 3 and C == 3:
            return "RICHARD"
        if R == 3 and C == 4:
            return "GABRIEL"
        if R == 4 and C == 1:
            return "RICHARD"
        if R == 4 and C == 2:
            return "RICHARD"
        if R == 4 and C == 3:
            return "GABRIEL"
        if R == 4 and C == 4:
            return "GABRIEL"
            
f = open("C:\Users\Owen\Documents\DEMAT\Google Code Jam\D-small-attempt0.in", "r")
a = []
for line in f:
    a.append(line)

    
for i in range(int(a[0])):
    arr = a[i+1].split(" ")
    print "Case #%s: %s" %(i+1, OminousOmino(int(arr[0]), int(arr[1]), int(arr[2])))