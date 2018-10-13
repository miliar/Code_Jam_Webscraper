'''
    Google Code Jam 2013
    Problem A: Bullseye
    
    @author: Masood Behabadi
'''

import math

data_file = "data/1-A-small-attempt0.in"

def find_rings(r, t):
      
    count = 0
    
    while (t > 0):
        t -= (2 * r) + 1
        count += 1
        r += 2
    
    if t < 0:
        count -= 1
            
    return count


if __name__ == '__main__':
    
    f = open(data_file, "r")
    
    ncase = int(f.readline())
    
    for c in range(ncase):
        
        r, t = f.readline().strip().split(" ")
        
        print 'Case #%d: %d' % (c + 1, find_rings(int(r), int(t)))
        