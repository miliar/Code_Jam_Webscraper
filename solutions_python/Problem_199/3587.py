def onlyHappy(pcList):
    count = 0;   
    for i in pcList:
        if i == '+':
            count = count + 1
    if count == len(pcList):
        return True
    else:
        return False

def flipSizePc(pcList, FlipperSize, start):
    pcListNew = list(pcList)

    for i in range(0, FlipperSize):
        if pcList[i+start] == '+':
            pcListNew[i+start] = '-'
        else:
            pcListNew[i+start] = '+'

    return "".join(pcListNew)

def findNextUnHappy(pcList):
    for i in range(0, len(pcList)):
        if pcList[i] == '-':
            return i;
    return -1;


def flipPancake(pcList, FlipperSize):
    if onlyHappy(pcList):
        return 0
    
    currentPcList = pcList
    i = 0
    while(1):
        ret = findNextUnHappy(currentPcList)
        #print("ret: "+str(ret))
        if ret == -1:
            break
        else:
            if FlipperSize+ret > len(currentPcList):
                #print ("Overflow")
                return -1
            else:
                currentPcList = flipSizePc(currentPcList, FlipperSize, ret)
                #print("currentPcList: "+currentPcList)
        
        i = i+1 
    
    print ("Final Pancake"+currentPcList+"Nb attempt: "+str(i)+"FilpperSize:"+str(FlipperSize))
    return i


if __name__ == "__main__":

    print ("Google Jam Pb1")

    infile = open("A-large.in", "r")
    outfile = open("A-large.out", "w")

    t = int(infile.readline())  
    for i in range(1, t + 1):
        l = infile.readline().split(" ")
        print ("Original"+l[0]+"case:"+str(i))
        nbAttempts = flipPancake(l[0], int(l[1][:-1]))
        if nbAttempts == -1:
            print("Case #{}: {}".format(i, "IMPOSSIBLE"), file = outfile)
        else:
            print("Case #{}: {}".format(i, nbAttempts), file = outfile)


