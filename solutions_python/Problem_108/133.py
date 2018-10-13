#!/usr/bin/env python
import sys
import numpy as np

infile=open(sys.argv[1],'r')

NumCases=int(infile.readline())

for iCase in xrange(NumCases):
    n,=[int(i) for i in infile.readline().split()]
    vines=[]
    for i in xrange(n):
        vines.append([int(i) for i in infile.readline().split()])
    vines.sort(key=lambda x:x[0])

    d,=[int(i) for i in infile.readline().split()]

    #print d
    #print vines
    heights={x[0]:-1 for x in vines}
    #print vines[0][0],vines[0][1],min( vines[0][0],vines[0][1] )
    heights[ vines[0][0] ] = min( vines[0][0],vines[0][1] )
    #print heights
    done=False
    answer='NO'
    while not done:
        changed=False
        for v in vines:
            if heights[v[0]]+v[0]>=d:
                answer='YES'
                done=True
                break

            if heights[v[0]]>0:
                for vv in vines:
                    if abs(vv[0]-v[0])<=heights[v[0]]:
                        oldheight=heights[vv[0]]
                        heights[vv[0]]=max( min( abs(vv[0]-v[0]), vv[1]),
                                            heights[vv[0]] )

                        if oldheight != heights[vv[0]]: changed=True
                        
        #print heights
        if answer=='YES': break
        if not changed:
            answer='NO'
            break


    print 'Case #'+str(iCase+1)+':',answer

