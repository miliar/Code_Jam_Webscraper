'''
Created on May 8, 2010

@author: francesccampoyflores
'''

import sys

if __name__ == '__main__':
    
    print sys.argv
    
    input = open(sys.argv[1], 'r')
    output = open(sys.argv[2],'w')
    
    T = int(input.readline())
    for t in range(1,T+1):
        N, K = map(int, input.readline().split())
        
        result = True
        for n in range(N):
            if K/2**n % 2 == 0:
                result = False
                break

        output.write("Case #%d: "%t)
        if result:
            output.write("ON\n")
        else:
            output.write("OFF\n")
        