import math

var = raw_input("Enter something: ").split('\n')
text = ""

caseno = 0
for line in var[1:]:
    if line != "":
        caseno += 1
        (R,C,W) = line.split(" ")
        R = int(float(R))
        C = int(float(C))
        W = int(float(W))

        tt = 0
        if C%W != 0:
            tt = 1
        score = C/W - 1 + W + tt
        newline = "Case #" + str(caseno) + ": " + str(score)
        text += "%s\n" % newline

#print text
filew = open("outputCode2.txt",'w')
filew.write(text)
filew.close()
