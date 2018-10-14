#!/usr/bin/env python
import sys
import numpy as np

if __name__ == '__main__':
    
    # Read data
    fh = file(sys.argv[1], 'r')
    n = int(fh.readline())
    for i in range(n):
        # Read data
        siz = int(fh.readline().split()[0])
        naomi = [ float(val) for val in fh.readline().split() ]
        ken = [ float(val) for val in fh.readline().split() ]
        
        # Sort
        naomi.sort()
        ken.sort()
        
        # Copy
        naomiwar = naomi[:]
        kenwar = ken[:]
        
        assert len(naomi) == siz
        assert len(naomi) == len(ken)
        
        # Deceitful war
        end = False
        while not end:
            
            # Check if winning
            win = True
            for k in range(len(ken)):
                if naomi[k] < ken[k]:
                    win = False
                    break
                    
            # Delete
            if not win and len(ken) > 0:
                naomi.pop(0)
                ken.pop(-1)
            elif not win and len(ken) == 0:
                dwar = 0
                end = True
            else:
                dwar = len(naomi)
                end = True
        
        # War
        war = 0
        end = False
        while not end:
            # Naomi choose
            nao = naomiwar.pop(0)
            
            # Ken choose
            found = False
            for j in range(len(kenwar)):
                if kenwar[j] > nao:
                    kenwar.pop(j)
                    found = True
                    break
            
            if not found:
                war += 1
                kenwar.pop(0)
                
            if len(kenwar) == 0:
                end = True

        # Result  
        print 'Case #%d: %d %d' % (i+1, dwar, war)
        
        #raw_input()
        
