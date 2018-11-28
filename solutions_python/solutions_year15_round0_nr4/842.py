import math

var = raw_input("Enter something: ").split('\n')
text = ""

caseno = 0
for line in var[1:]:
    if line != "":
        caseno += 1
        (X,R,C) = line.split(" ")
        X = int(float(X))
        R = int(float(R))
        C = int(float(C))
        if X == 1:
            winner = "GABRIEL"
        elif (R*C) % X != 0:
            winner = "RICHARD"
        elif X > 2 and (math.sqrt(X) >= R or math.sqrt(X) >= C):
            winner = "RICHARD"
        elif X > 6:
            winner = "RICHARD"
        else:
            winner = "GABRIEL"
        newline = "Case #" + str(caseno) + ": " + str(winner)
        text += "%s\n" % newline
        if winner == "GABRIEL":
            print line
print text
filew = open("outputCode2.txt",'w')
filew.write(text)
filew.close()
