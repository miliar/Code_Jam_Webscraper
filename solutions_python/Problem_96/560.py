import time

debug = True

tStart = time.time()

fname = "B-large"
#fname = "dance"

fin = open(fname+".in","r")
flines = fin.readlines()
fin.close()

fout = open(fname+".out","w")

numcases = int(flines[0])

for icase in range(1,numcases+1):
    line = flines[icase].split()
    bigN = int(line[0])
    bigS = int(line[1])
    targetp = int(line[2])
    dancers = [0]*(bigN)
    for x in range(bigN):
        dancers[x] = int(line[3+x])
    
    sleft = bigS
    quals = 0
    #print dancers

    for j in range(bigN):
        if dancers[j] >= targetp:
            # Guard the low end.  If this isn't the case, then this
            # dancer could NOT have achieved the goal.
            targ = 3*targetp
            if dancers[j] >= max(0,targ-2):
                quals += 1
            elif dancers[j] >= max(0,targ-4) and sleft > 0:
                quals += 1
                sleft -= 1

    outstr = "Case #%d: %d" % (icase,quals)
    print outstr
    fout.write("%s\n" % (outstr))
    
fout.close()

tEnd = time.time()

print "run time = %s" % (str((tEnd - tStart)))
