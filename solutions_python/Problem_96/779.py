import sys
import math

def procCase( nums ): 
    N = nums[0]
    S = nums[1]
    p = nums[2]

    if N == 0:
        return 0

    aboveP = 0
    for x in range( 3, len(nums) ):
        x = nums[ x ]
        if x >= p and x >= (p * 3 - 4):
            if x >= (p * 3 - 2): 
                aboveP += 1
            elif S > 0:
                aboveP += 1
                S -= 1 
                
    return aboveP

        

cnt = 0
for l in sys.stdin.readlines():
    if cnt > 0:
        numbers = map( lambda x: int( x ) , l.split() )
        print "Case #" + str( cnt ) + ": " + str( procCase(numbers) ) 
    cnt = cnt + 1 
