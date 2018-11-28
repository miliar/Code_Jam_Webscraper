from __future__ import division
import time
#t0=time.clock()

t = int(raw_input())  # read a line with a single integer
for tr in xrange(1, t + 1):
    dest, numhorses = [s for s in raw_input().split(" ")]
    dest=int(dest)
    numhorses=int(numhorses)
    tmax=0
    for i in xrange(numhorses):
        desthorse,speedhorse= [s for s in raw_input().split(" ")]
        desthorse=int(desthorse)
        speedhorse=int(speedhorse)
        
        thorse=(dest-desthorse)/speedhorse
        tmax=max(tmax,thorse)
    
    speedAnna=dest/tmax
       
    print "Case #{}: {}".format(tr, speedAnna)
#print time.clock()-t0