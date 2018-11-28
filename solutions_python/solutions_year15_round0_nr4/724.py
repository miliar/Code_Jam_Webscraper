def OminousOmino(X, R, C):
    """docstring for OminousOmino"""
    if R * C % X != 0:
        return "RICHARD"
    elif X == 1:
        return "GABRIEL"
    elif X == 2:
        return "GABRIEL"
    elif X == 3:
        if R == 1 or C == 1:
            return "RICHARD"
        else:
            return "GABRIEL"
    elif X == 4:
        if C * R == 4:
            return "RICHARD"
        elif C * R == 8:
            return "RICHARD"
        elif C * R == 12:
            return "GABRIEL"
        elif C * R == 16:
            return "GABRIEL"

if __name__ == "__main__":
    f = open("D-small-attempt2.in")
    i = 0
    wr = open("res.txt", "w")
    for line in f:
        if i == 0:
            i = i + 1
            continue
        X, R, C = line.split()
        X = int(X)
        R = int(R)
        C = int(C)
        wr.write("Case #" + str(i) + ": " + OminousOmino(X, R, C) + "\n")
        i = i + 1
    f.close()
    wr.close()
