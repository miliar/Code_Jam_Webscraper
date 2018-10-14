def processcase(clist,olist,invoke):
    index = 0 
    output = "["
    outlist = []
    while index < len(invoke):
        outlist.append(invoke[index])
        if len(outlist) > 1:
            outlist = combchecker(clist,outlist)
            outlist = opposechecker(olist,outlist)
        index += 1
    for i in outlist:
        output += i+","+" "
    if len(output) > 1:
        output= output[0:-2]
    output += ']'
    return output
        
        
def combchecker(clist,outlist):
    e1 = outlist[-1]
    e2 = outlist[-2]
    for x in clist:
        if (x[0]== e1 and x[1]==e2) or (x[1]== e1 and x[0]==e2):
            outlist = outlist[0:-2]
            outlist.append(x[2])
    return outlist
    

def opposechecker(olist,outlist):
    e = outlist[-1]
    for x in olist:
        for y in outlist[0:-1]:
            if (e == x[0] and y == x[1]) or (e == x[1] and y == x[0]):   
                return []
    return outlist


def inputfilter(filename):
    finput = open(filename,'r')
    fout = open("out.txt",'w')
    casenum = int(finput.readline())
    for i in range(1,casenum+1):
        inlist = finput.readline().split()
        combinelist = []
        opposelist = []
        invokelist = ""
        tmplist = combinelist
        num = 0
        index = 0
        while index < len(inlist):
            if inlist[index].isdigit() and num < 2:
                for j in range(0,int(inlist[index])):
                    tmplist.append(inlist[index+1])
                    index += 1
                num += 1
                tmplist = opposelist
            index += 1
        invokelist = inlist[-1]
        fout.write("Case #"+str(i)+": "+processcase(combinelist,opposelist,invokelist)+'\n')
        print "Case #"+str(i)+": "+processcase(combinelist,opposelist,invokelist)+'\n'
    finput.close()
    fout.close()

    
if __name__=="__main__":
    inputfilter("B-large.in")