'''
Created on Apr 11, 2014

@author: di
'''

import sys

casesnum = (int)(sys.stdin.readline());

arrangement1 = list()
arrangement2 = list()
row1 = -1
row2 = -1

case = 1

while case <= casesnum:
    row1 = (int)(sys.stdin.readline())
    arrangement1.append(sys.stdin.readline().split())
    arrangement1.append(sys.stdin.readline().split())
    arrangement1.append(sys.stdin.readline().split())
    arrangement1.append(sys.stdin.readline().split())
    #print row1, arrangement1
    row2 = (int)(sys.stdin.readline())
    arrangement2.append(sys.stdin.readline().split())
    arrangement2.append(sys.stdin.readline().split())
    arrangement2.append(sys.stdin.readline().split())
    arrangement2.append(sys.stdin.readline().split())
    #print row2, arrangement2
    
    common = [ x for x in arrangement1[row1-1] if x in arrangement2[row2-1]]
    #print common
    if len(common) == 1:
        print "Case #"+str(case)+": " + common[0]
    elif len(common) > 1:
        print "Case #"+str(case)+": Bad magician!"
    else:
        print "Case #"+str(case)+": Volunteer cheated!"
    arrangement1 = []
    arrangement2 = []
    case += 1;
