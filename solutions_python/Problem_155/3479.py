def solver(Smax, audience):
    s = 0
    x = 0
    for i in range(0, Smax + 1):
        number = int(audience[i])
        if number > 0:
            if i > s:
                x = x + (i - s)
            else:
                x = x
            s = s + number + x
    return x

def readandwrite():
    inputtxt = open('/Users/yongeun/Dropbox/Code_Jam_2015/A-small-attempt0.in','r')
    outputtxt = open('/Users/yongeun/Dropbox/Code_Jam_2015/A-small-attempt0.out','w')
    T = int(inputtxt.readline())
    for k in range(0, T):
        line = inputtxt.readline()
        Smax = int(line[0])
        audience = line[2:]
        outputtxt.write('Case #'+str(k+1)+': '+str(solver(Smax,audience))+'\n')    
        
readandwrite()
