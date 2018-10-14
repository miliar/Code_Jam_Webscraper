#
# Google Code Jam 2015
# Roaund 0: B. Infinite House of Pancakes
# submission by EnTerr
#

'''

Input 
3
1
3
4
1 2 1 2
1
4
 	
Output 
Case #1: 3
Case #2: 2
Case #3: 3

'''



import sys
from time import clock


f = open(sys.argv[1])
def input(): return f.readline().strip();

       
def getMinMinutes(plates, cache = { }):
    if not plates: return 0
    
    plates.sort()
    # max - the last element - is upper limit on min number of steps
    mx = plates[-1]
    if mx < 4: return mx    # no use in splitting 2, 3
    
    # check if we already solved that
    kee = tuple(plates)
    res = cache.get(kee)
    if not res:
        res = min(mx, \
                1 + getMinMinutes(plates[:-1] + [mx // 2, mx - mx // 2]), \
                1 + getMinMinutes(plates[:-1] + [mx // 3, mx - mx // 3]), \
                )
        #cache[kee] = res        

    return  res
	

#clk = clock()

for caseNo in xrange(1, int(input())+1):
    input() # skip #plates, assumed
    plates = map(int, input().split())
#    print >>sys.stderr, caseNo
    print 'Case #%d:' % caseNo, getMinMinutes(plates)
    
#print >>sys.stderr, 'time= %.1f seconds' % (clock()-clk )

