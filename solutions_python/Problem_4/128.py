import math

def solve(fstr):
    outStr = ""
    ipt = fstr.strip().split('\n')
    ipt = ipt[1:]
    iptInd = 0
    tcInd = 0
    while iptInd < len(ipt):
        tcInd += 1
        v1 = ipt[iptInd+1].split()
        v2 = ipt[iptInd+2].split()
        for i in range(len(v1)):
            v1[i] = int(v1[i])
        for i in range(len(v2)):
            v2[i] = int(v2[i])
        
        v1.sort()
        
        v2.sort()
        v2.reverse()
        
        s = 0
        for i in range(len(v1)):
            print v1[i],v2[i]
            s += v1[i]*v2[i]
        
        print s
        
        iptInd += 3
                
        outStr += "Case #" + str(tcInd) +": " + str(s) + "\n"

    return outStr
    

ipt = None
opt = None
iptF = None
try:
    prog = "A"
    fName = "A-large.in"
    iptF = file("C:\eclipse-SDK-3.3.2-win32\GCJ\\" + prog + "\\" + fName)
    outStr = solve(iptF.read())
    print outStr
    optF = file("C:\eclipse-SDK-3.3.2-win32\GCJ\\" + prog + "\output.txt",'w+')
    optF.write(outStr)
    optF.close()
    if (fName == "input.txt"):    
        otstF = file("C:\eclipse-SDK-3.3.2-win32\GCJ\\" + prog + "\outtest.txt")
        otst = otstF.read()
        otstF.close()
        if (otst == outStr):
            print "+++++++++++++++ CORRETO +++++++++++++++++"
        else:
            print "______________ INCORRETO ________________"
finally:
    if (iptF != None):
        iptF.close()
