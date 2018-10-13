import sys
try:
    fname = sys.argv[1]
except:
    print("input filename")
    sys.exit(1)
infile = open(fname)
outfile = open("out","w")
numtry = int(infile.readline())
for ctry in range(0, numtry):
    cps = 2
    t = 0
    (C, F, X) = map(float, infile.readline().split(' '))
    print(C, F, X)
    mintime = X / cps
    endtime = mintime
    while True:
        curtime = X / cps + t
        #print(curtime)
        if curtime < mintime:
            mintime = curtime
        t += C / cps
        cps += F
        if t>endtime:
            break
        if (C/cps - C/(cps+F)) < 1e-8:
            break
               
    
    textout = "Case #%d: %.7f" % (ctry+1, mintime)
    print(textout)
    outfile.write(textout+'\n')
outfile.close()    
infile.close()
