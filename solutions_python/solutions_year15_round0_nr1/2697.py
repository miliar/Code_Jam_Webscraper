# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 18:42:16 2015

@author: Oliver
"""

def getNum(text):
    added, have = 0, 0
    for idx, i in enumerate(text):
        if (have < idx):
            added += idx - have
            have += idx - have
        have += int(i)
        
    return added
    
fo = open('large_out.txt', 'wb')

with open('A-large.in') as f:
    count = 1
    for line in f:
        if (len(line.split()) == 2):
            fo.write( 'Case #%d: %d\n' % (count, getNum(line.split()[1]) ) )
            count += 1
            
    fo.close()