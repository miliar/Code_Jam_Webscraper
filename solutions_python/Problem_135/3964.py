
import os
import sys
from sets import Set

t = int(sys.stdin.readline().strip())
for icase in range(t):

    # arrangement 1
    i1 = int(sys.stdin.readline().strip())
    l1 = []
    for i in range(4):
        line = sys.stdin.readline().strip().split(' ')
        l1.append(line)

    # arrangement 2
    i2 = int(sys.stdin.readline().strip())
    l2 = []
    for i in range(4):
        line = sys.stdin.readline().strip().split(' ')
        l2.append(line)

    # Intersection
    s1 = Set(l1[i1-1])
    s2 = Set(l2[i2-1])
    
    cards = s1 & s2
    ncards = len(cards)
     
    print "Case #%i:"%(icase+1), 
    if ncards==0:
        print "Volunteer cheated!"
    elif ncards==1:
        print cards.pop()
    else:
        print "Bad magician!"
