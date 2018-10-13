def main():
    f = open("input.txt",'r')
    lines = f.readlines()
    lines = map(lambda x: x.rstrip("\n"),lines)
    f.close()
    count = int(lines[0])
    i = 1
    output = ""
    while i<=count:
        stepQueue = []
        command = lines[i].split(" ")
        combines = getCombines(command)
        opposed = getOpposed(command)
        command.remove(command[0])
        res = procComb(command[0], combines, opposed)
        output += "Case #%d: %s\n" %(i,toGList(res))
        i+=1
    output = output[:len(output)-1]
    print output
    f = file("output.txt","w")
    f.write(output)
    f.close()

def getCombines(data):
    out = {}
    numCombines = int(data[0])
    data.remove(data[0])
    i = 0
    while i<numCombines:
        cE = data[0]
        elems = list(cE[0:2])
        elems.sort()
        res = cE[2]
        out["".join(elems)] = res
        data.remove(cE)
        i+=1
    return out
def getOpposed(data):
    out = []
    numOpposed = int(data[0])
    data.remove(data[0])
    i = 0
    while i<numOpposed:
        cE = data[0]
        elems = list(cE[0:2])
        elems.sort()
        out.append("".join(elems))
        data.remove(cE)
        i+=1
    return out

def procComb(com, combines, opposed):
    eList = []
    for s in com:
        chkCom(eList, s, combines)
        chkOpp(eList, opposed)
    return eList
def chkCom(eList, new, combines):
    if len(eList)==0:
        eList.append(new)
        return
    cList = [eList[len(eList)-1], new]
    cList.sort()
    cStr = "".join(cList)
    if cStr in combines:
        eList.pop()
        eList.append(combines[cStr])
    else:
        eList.append(new)
def chkOpp(eList, opposed):
    lElem = eList[len(eList)-1]
    for x in eList:
        oL = [lElem, x]
        oL.sort()
        if "".join(oL) in opposed:
            del eList[:]

def toGList(eList):
    if eList == []: return "[]"
    out = "["
    for x in eList:
        out += str(x) + ", "
    out = out[:len(out)-2]
    out += "]"
    return out

if __name__=="__main__":
    main()
