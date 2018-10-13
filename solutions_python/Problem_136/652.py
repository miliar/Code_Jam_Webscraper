'''
Created on Apr 12, 2014

@author: di
'''

import sys

casesnum = (int)(sys.stdin.readline());

case = 1

while case <= casesnum:
    C, F, X = [float(x) for x in sys.stdin.readline().split()]
    Time1 = 0;
    Time2 = 0;
    
    farms = 0;
    total = 0;
    
    while Time1 >= Time2:
        Time1 = X / (2 + farms * F)
        Time2 = C / (2 + farms * F) +  X / (2 + (farms + 1) * F)
        if farms - 1 >= 0: 
            total += C / (2 + (farms - 1) * F)
        farms += 1
    total += Time1
    print "Case #"+str(case)+": %.7f" % total
    case += 1