import sys
from copy import copy
from collections import deque
from time import sleep

qty_test_cases = int(sys.stdin.readline())

for i in range(qty_test_cases):
    print "Case #%d:" % (i+1),
    
    players, low, high = [int(x) for x in sys.stdin.readline().strip().split(" ")[0:3]]
    notes = [int(x) for x in sys.stdin.readline().strip().split(" ")[0:players]]
    
    for j in range(low,high+1):
        broken = False
        for note in notes:
            if (j % note if note < j else note % j) != 0:
                broken = True
                break
        
        if not broken:
            print j
            break
    
    if broken:
        print "NO"

