
'''
Created on Apr 12, 2013

@author: herman
'''


infile = open("input.txt","r")
outfile = open("output.txt","w")

trials = int(infile.readline())

PMAX = 1000

def splits_to_target(pans,target):
    total = 0
    for p in pans:
        if p > target:
            total += (p/target) + int(p % target != 0) -1
    return total
    
def pan_time(pans):
    all_times = [splits_to_target(pans,t)+t for t in xrange(1,PMAX+1)]
    return min(all_times)
    
for i in xrange(trials):
    D = int(infile.readline())
    pans = [int(x) for x in infile.readline().split()]

    s = "Case #%d: %d\n" % (i+1,pan_time(pans))
    outfile.write(s)
    print s
    
infile.close()
outfile.close()
