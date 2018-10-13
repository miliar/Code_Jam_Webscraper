def getCombo(el, elList, combos):
    if len(elList) is not 0:
        for x in combos:
            if el == x[0]:
                if elList[-1] == x[1]:
                    return x[2]
            elif el == x[1]:
                if elList[-1] == x[0]:
                    return x[2]
    return ""

def containsOpposed(elList, opposed):
    copy = list(elList)
    for x in opposed:
        if x[0] in copy:
            copy.remove(x[0])
            if x[1] in copy:
                return True
    return False
    

def invokeElement(el, elList, combos, opposed):
    c = getCombo(el, elList, combos)
    if not c is "":
        elList.pop()
        elList.append(c)
    else:
        elList.append(el)
    if containsOpposed(elList, opposed):
        elList = []
    return elList


def processLine(line):
    combos = []
    opposed = []
    # parse it
    splitline = line.split(" ")
    
    # find combos
    cnum = int(splitline[0])
    splitline = splitline[1:]
    for i in range(cnum):
        combos.append(splitline[i])
    splitline = splitline[cnum:]
    
    # find opposed
    onum = int(splitline[0])
    splitline = splitline[1:]
    for i in range(onum):
        opposed.append(splitline[i])
    splitline = splitline[onum:]
    
    # find elements
    elements = splitline[1]

    # invoke
    elList = []
    for e in elements:
        elList = invokeElement(e, elList, combos, opposed)

    return elList

towrite=[]
with open('C:\\Users\\Steph\\Desktop\\actualinput.txt', 'r') as f:
    lines = f.readlines()
    for l in lines[1:]:
        a = l
        if "\n" in a:
            a = l[:-1]
        result = processLine(a)
        towrite.append(result)

with open('C:\\Users\\Steph\\Desktop\\answer.txt', 'w') as f:
    i = 1
    for w in towrite:
        if i is not 1:
            f.write("\n")
        a = "["
        for x in w:
            a += x + ", "
        if len(a)>1:
            a = a[:-2]
        a+= "]"
        answer = "Case #" + str(i) + ": " + a
        print answer
        f.write(answer)
        i +=1
    


