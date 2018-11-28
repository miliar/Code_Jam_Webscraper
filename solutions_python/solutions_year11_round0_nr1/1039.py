
import numpy as np



def friend(robot):
    return 'O' if robot == 'B' else 'B'


fin = file("A-large-0.in")
fout = file ("A-large-0.out", "w")
fin.readline()

for i, line in enumerate(fin):
    targets = line.strip().split()[1:]
    targets = np.reshape(targets, (-1, 2))

    pos = {'O' : 1, 'B' : 1 }
    waiting = {'O' : 0, 'B' : 0 }
    totalTime = 0
    for h, nstr in targets:
        n = int(nstr)
        dist = abs(n - pos[h])
        time = max(0, dist - waiting[h]) + 1

        waiting[h] = 0
        waiting[ friend(h) ] += time
        
        totalTime += time
        #print "%s: %i -> %i, dist = %i,  time = %i, totalTime = %i" % (h, pos[h], n, dist, time, totalTime)

        pos[h] = n

    outStr = "Case #%i: %i" % (i+1, totalTime)
    #print line, outStr
    fout.write(outStr + "\n")

fout.close()
        
