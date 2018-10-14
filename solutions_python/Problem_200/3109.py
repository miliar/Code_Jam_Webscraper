def strtoarray(xstr):
    return [int(d) for d in str(xstr)]

def checkTidy(x):
    for i in np.arange(1,len(x)):
        if int(x[i])<int(x[i-1]):
            return False        
    return True

def makeTidy(xstr):
    xarr = strtoarray(xstr)
    if checkTidy(xarr)==True:
        return xstr
    else:
        isTidy = False
        while isTidy==False:
            for i in np.arange(1,len(xarr)):
                if int(xarr[i])<int(xarr[i-1]):
                    xarr[i-1] = xarr[i-1] - 1
                    xarr[i:len(xarr)] = [9 for j in xarr[i:len(xarr)]]
                    break
            if checkTidy(xarr)==True:
                isTidy = True
        if xarr[0]==0:
            xarr = xarr[1:]
        return ''.join(str(e) for e in xarr)
                    
def solveC():
    inputarr = np.loadtxt('B-small-attempt0.in')
    outputarr = list()
    T = int(inputarr[0])
    for i in np.arange(1,T+1):
        tidy = makeTidy(str(int(inputarr[i])))
        outputarr.append('Case #'+str(i)+': '+str(tidy))
        
    # Write to file
    with open("probCsmallout.txt", "w") as output:
        for item in outputarr:
            output.write("%s\n" % item)        

solveC()