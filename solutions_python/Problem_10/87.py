import sys,math
import psyco
psyco.full()

    
lines = sys.stdin.readlines()
it = iter(lines)
num = int(it.next())
for i in range(num):
    case = 1+i
    line = it.next()
    numLet,keys,numAlpha = [int(i) for i in line.split()]
    line = it.next()
    alphabetFreq = reversed(sorted([int(i) for i in line.split()]))
    if numAlpha > numLet*keys:
        print "Case #"+str(case)+": Impossible"
    else:
        key = 0
        r = 1
        presses = 0
        for let in alphabetFreq:
            presses += let*r
            key += 1
            if key == keys: 
                key = 0
                r += 1
        print "Case #"+str(case)+": "+str(presses)

