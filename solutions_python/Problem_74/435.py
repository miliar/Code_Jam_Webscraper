import sys
import math

count = 1
for line in sys.stdin.readlines()[1:]:
    entries = line.strip().split(' ')
    pairs = zip(entries[1::2], entries[2::2])

    bPos = 1
    oPos = 1
    
    bLast = 0
    oLast = 0
    
    time = 0

    for (robot, pos) in pairs:
        pos = int(pos)
        if robot == 'O':
            toMove = math.fabs(oPos-pos)
            
            timeDiff = time - oLast
            
            if timeDiff >= toMove:
                time +=1
                oLast = time
                oPos = pos
            else:
                time = oLast + toMove + 1
                oLast = time
                oPos = pos
        else:
            toMove = math.fabs(bPos-pos)
            
            timeDiff = time - bLast
            
            if timeDiff >= toMove:
                time +=1
                bLast = time
                bPos = pos
            else:
                time = bLast + toMove + 1
                bLast = time
                bPos = pos
        

    print "Case #" + str(count) + ": " + str(int(time))
    count += 1 
