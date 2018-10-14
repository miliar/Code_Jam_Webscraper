'''
Created on May 22, 2010

@author: francesccampoyflores
'''

import sys

debug = True


if __name__ == '__main__':
    input = open(sys.argv[1],'r')
    output = open(sys.argv[2], 'w')
    
    C = int(input.readline())
    
    for c in range(1, C+1):
        N, K, B, T = map(int, input.readline().split())
        location = map(int, input.readline().split())
        speed =  map(int, input.readline().split())
        
        final_location = [location[i]+speed[i]*T for i in range(N)]
        
        arrived = len(filter(lambda x: x>=B, final_location))
        
        if debug:
            print "Case %d"%c
            print "N : %d, K : %d, B : %d, T : %d"%(N, K, B, T)
            print location
            print speed
            print final_location
            print map(lambda x: x-B, final_location)

        
        if arrived < K:
            output.write("Case #%d: IMPOSSIBLE\n"%(c))
            if debug:
                print "Case #%d: IMPOSSIBLE"%(c)
        else :
            final_location.reverse()
            
            slow = 0
            swaps = 0
            arriving = K
            
            for p in final_location:
                if p < B:
                    slow += 1
                else:
                    arriving -= 1
                    swaps += slow
                if arriving == 0:
                    break
                
            output.write("Case #%d: %d\n"%(c, swaps))
            if debug:
                print "Case #%d: %d"%(c, swaps)
        