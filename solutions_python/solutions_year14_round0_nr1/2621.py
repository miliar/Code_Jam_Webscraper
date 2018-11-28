'''
Created on Apr 12, 2014

@author: fuellerm
'''

import sys

# Read one 4x4 block of cards
def read_cards(f):
    row = int(f.readline())
    for j in range(1, 5):
        if j == row:
            result = set(f.readline().rstrip('\n').split(' '))
        else:
            f.readline()
    return result

f = open(sys.argv[1], 'r')
n = int(f.readline())
for i in range(1, n+1):
    cards1 = read_cards(f)
    cards2 = read_cards(f)    
    common = list(cards1 & cards2)
    
    if len(common) == 0:
        result = "Volunteer cheated!"
    elif len(common) == 1:
        result = common[0]
    else:
        result = "Bad magician!"
        
    print "Case #" + str(i) + ": " + result
            
    