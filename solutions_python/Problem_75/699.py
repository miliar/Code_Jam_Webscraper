import copy

def function2(fi,fo):
    f = open(fi)
    f2 = open(fo,"w")
    cases = int(f.readline())
    for nc,case in enumerate(range(cases)):
        test = f.readline()[0:-1].split(" ")
        elements = ["Q","W","E","R","A","S","D","F"]
        elementList = []
        combinations = {}
        oposites = {}
        for i in elements:
            oposites[i] = []
        C = int(test[0])
        pos = 1
        for i in range(C):
            st = test[pos]
            combinations[(st[0],st[1])] = st[2]
            combinations[(st[1],st[0])] = st[2]
            pos += 1
        D = int(test[pos])
        pos += 1
        for i in range(D):
            st = test[pos]
            oposites[st[0]] += [st[1]]
            oposites[st[1]] += [st[0]]
            pos += 1
        N = int(test[pos])
        pos += 1
        call = test[pos]
        elementList = [call[0]]
        elPos = 1
        searchOp = True
        while elPos < len(call):
            element = call[elPos]
            if len(elementList)>0:
                if combinations.has_key((elementList[-1],element)):
                    elementList[-1] = combinations[(elementList[-1],element)]
                    elPos += 1
                else:
                    ops = oposites[element]
                    isop = False
                    for j in ops:
                        if j in elementList:
                            isop = True
                            break
                    if isop:
                        elementList = []
                    else:
                        elementList += [element]
                    elPos += 1
            else:
                elementList += [element]
                elPos += 1
        elementList = str(elementList).replace("'","")
        text = "Case #" + str(nc+1) + ": "  + str(elementList)
        f2.write(text + "\n")
        

#function2("magick.in","test.txt")
#function2("short.in","short.txt")
function2("long.in","long.txt")

