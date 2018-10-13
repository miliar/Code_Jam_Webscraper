f = open('D-small-attempt0.in', 'r')
g = open('output4.txt', 'w')

def getVal(X,R,C):
    if X > 6:
        return "RICHARD"
    elif (X > R and X > C) or (2*min(R,C) < X):
        return "RICHARD"
    elif X == 1:
        return "GABRIEL"
    elif (R*C)%X != 0:
        return "RICHARD"
    elif X==2:
        return "GABRIEL"
    elif X==3:
        return "GABRIEL"
    #since we've already determined that (R*C)%X==0, so R or C must divide by 3
    elif X==4:
        if (R==2 or C==2):
            return "RICHARD"
        else:
            return "GABRIEL"
    return "WTF"

num = int(f.readline())
for i in range (num):
    data = f.readline().split()
    X = int(data[0])
    R = int(data[1])
    C = int(data[2])

    s = "Case #" + str(i+1) + ": " + getVal(X,R,C) + '\n'
    g.write(s)

f.close()
g.close()




