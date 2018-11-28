

def getWinner(X,R,C):
    if X ==1 :
        return "GABRIEL"
    elif X == 2 :
        if R % 2 == 0 or C % 2 == 0:
            return "GABRIEL"
        else:
            return "RICHARD"
    elif X == 3:
        if (R % 3 == 0 or C % 3 == 0) and R+C > 4:
            return "GABRIEL"
        else:
            return "RICHARD"
    elif X == 4:
        if (R % 4 == 0 or C % 4 == 0) and R+C > 6:
            return "GABRIEL"
        else:
            return "RICHARD"

f = open("one.in", "r").read()

#new_file = open("sma.txt", "w")
splitted_file = f.split("\n")[:]

lineCounter =1
amountOfLines = len(splitted_file)

case = 0

while(lineCounter < amountOfLines):
    case += 1
    firstLine = splitted_file[lineCounter]
    lineCounter += 1
    
    X,R,C = firstLine.split(" ")
    X,R,C = [int(X), int(R), int(C)]
    out = getWinner(X,R,C)
    print "Case "+ "#"+str(case) +": " + out
    
    
