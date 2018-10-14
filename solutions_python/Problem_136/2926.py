fh = open("B-large.in", "r")
fh2 = open("cookiecutteralphaoutputlarge.txt", "w")
testCases = fh.readline()

for i in xrange(int(testCases)):
    nextline = fh.readline()
    C = float(nextline[0: nextline.index(" ")])
    nextline = nextline[nextline.index(" ") + 1:]
    F = float(nextline[0: nextline.index(" ")])
    nextline = nextline[nextline.index(" ") + 1:]
    X = float(nextline)

    t = 0.0
    R = 2.0

    while X / R >= C / R + X / (R + F):
        t += C / R
        R += F
        
    t += X / R
    fh2.write("Case #" + str(i + 1) + ": " + str('%.7f' % t) + "\n")
    

fh.close()
fh2.close()
    
    
    
        
