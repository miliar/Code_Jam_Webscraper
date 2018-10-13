import time
def dijkstra(inputfile, outputfile):
    print "bezig"
    tijd_start = time.time()
    inputdata = open(inputfile, "r")
    outputdata = open(outputfile, "w")
    T = int(inputdata.readline())
    for case in range(T):
        #read input
        L,X = map(int,inputdata.readline().split())
        to_reduce = inputdata.readline().strip()
        #probleem
        print "Lengte: ",str(X),str(L),str(X*L)
        volledige_string = to_reduce * X
        outpt = is_solveable(volledige_string)
        if outpt:
            antwoord = "YES"
        else:
            antwoord = "NO"
        print "Case #" + str(case+1) + ": " + antwoord
        outputdata.write("Case #" + str(case+1) + ": " + antwoord + "\n")
    inputdata.close()
    outputdata.close()
    print "done", time.time()-tijd_start

def vermenigvuldig(x,y):
    if x[1] == "1":
        return (x[0]*y[0],y[1])
    elif x[1] == y[1]:
        return (x[0]*y[0]*-1,"1")
    elif y[1] == "1":
        return (x[0]*y[0],x[1])
    elif x[1] == "i":
        if y[1] == "j":
            return (x[0]*y[0],"k")
        elif y[1] == "k":
            return (x[0]*y[0]*-1,"j")
    elif x[1] == "j":
        if y[1] == "i":
            return (x[0]*y[0]*-1,"k")
        elif y[1] == "k":
            return (x[0]*y[0],"i")
    elif x[1] == "k":
        if y[1] == "i":
            return (x[0]*y[0],"j")
        elif y[1] == "j":
            return (x[0]*y[0]*-1,"i")
    print "probleem bij maal",x,y

def deel(x,y):
    #x*antwoord = y
    if x[1] == "1":
        return (x[0]*y[0],y[1])
    elif x[1] == y[1]:
        return (x[0]*y[0],"1")
    elif y[1] == "1":
        return (x[0]*y[0]*-1,x[1])
    elif x[1] == "i":
        if y[1] == "j":
            return (x[0]*y[0]*-1,"k")
        elif y[1] == "k":
            return (x[0]*y[0],"j")
    elif x[1] == "j":
        if y[1] == "i":
            return (x[0]*y[0],"k")
        elif y[1] == "k":
            return (x[0]*y[0]*-1,"i")
    elif x[1] == "k":
        if y[1] == "i":
            return (x[0]*y[0]*-1,"j")
        elif y[1] == "j":
            return (x[0]*y[0],"i")
    print "probleem bij delen",x,y


def calc_string(stringding):
    result = (1,"1")
    for letter in stringding:
        result = vermenigvuldig(result,(1,letter))
    return result

def is_solveable(volledige_string):
    resultaat1 = (1,"1")
    resultaat2 = (1,"1")
    resultaat3 = calc_string(volledige_string[1:])
    resultaat3t = resultaat3
    vorige_calc = 0
    for i in xrange(len(volledige_string)-2):
        resultaat1 = vermenigvuldig(resultaat1,(1,volledige_string[i]))
        if resultaat1[0] == 1 and resultaat1[1] == "i":
            resultaat2 = (1,"1")
            resultaat3 = resultaat3t
            for j in xrange(len(volledige_string[i:])-2):
                resultaat2 = vermenigvuldig(resultaat2,(1,volledige_string[i+j+1]))
                vorige_calc += 1
                if resultaat2[0] == 1 and resultaat2[1] == "j": 
                    resultaat3 = deel(calc_string(volledige_string[i+j-vorige_calc+2:i+j+2]),resultaat3)
                    vorige_calc = 0
                    if resultaat3[0] == 1 and resultaat3[1] == "k":
                        return True
            vorige_calc = 0
        resultaat3t = deel((1,volledige_string[i+1]),resultaat3t)

    else:
        return False



#dijkstra("input.txt","output.txt")
dijkstra("Cs4.in","outputs4v3.txt")
#v1 160 274 251
#v2 050 084 120 059
#v3 120 209 192 136
