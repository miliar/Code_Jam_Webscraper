#!/usr/bin/env python
# -*- coding=utf-8 -*-

import sys



def main():
    # get num of cases
    n = int(sys.stdin.readline())
    for case in range(n):
        process(case)
        
def move(robot, dest):
    if robot < dest:
        return robot+1
    else:
        return robot-1

def pushstay(robot):
    pass

def process(case):
    seq = sys.stdin.readline().split()
    #print seq

    orange = 1
    blue = 1

    orangelist = []
    bluelist = []

    for i,elem in enumerate(seq[1:len(seq):2]):
        #print seq[(i+1)*2],elem
        if elem == 'O' :
            orangelist.append((i,int(seq[(i+1)*2])))
        else :
            bluelist.append((i,int(seq[(i+1)*2])))
        
    #print orangelist, bluelist
    
    c = 0
    n = 0
    while orangelist or bluelist:
        if len(orangelist) == 0:
            if bluelist[0][1] == blue:
                bluelist.pop(0)
                n += 1
            else:
                # move!
                blue = move(blue, bluelist[0][1])
        elif len(bluelist) == 0:
            if orangelist[0][1] == orange:
                orangelist.pop(0)
                n += 1
            else:
                # move!
                orange = move(orange, orangelist[0][1])
        else:
            if orangelist[0][0] == n:
                # orange turn!
                if orangelist[0][1] == orange:
                    # push!
                    orangelist.pop(0)
                    n += 1
                else:
                    # move!
                    orange = move(orange, orangelist[0][1])

                if bluelist[0][1] == blue:
                    # stay!
                    pass
                else:
                    # move!
                    blue = move(blue, bluelist[0][1])
            else:
                # blue turn!
                if orangelist[0][1] == orange:
                    # stay!
                    pass
                else:
                    # move!
                    orange = move(orange, orangelist[0][1])

                if bluelist[0][1] == blue:
                    # push!
                    bluelist.pop(0)
                    n += 1
                else:
                    # move!
                    blue = move(blue, bluelist[0][1])

        c += 1
            
    # print result
    print("Case #{0}: {1}".format(case+1, c))
        
    
main()
