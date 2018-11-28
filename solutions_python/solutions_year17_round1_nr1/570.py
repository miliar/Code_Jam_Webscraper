# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 19:33:12 2017

@author: Tom
"""

import itertools


#fname = 'a.in'
fname = 'A-large.in'
oname = fname[:-3]+'.out'
with open(fname,'r') as f:
    with open(oname,'w') as o:
        T = int(f.readline().strip())
        for case in range(1,T+1):
            print('Case #{}:'.format(case))
            temp = [int(x) for x in f.readline().strip().split(' ')]
            R = temp[0]
            C = temp[1]
            cake = []  # one dimensional list = array
            for row in range(R):
                derp = list(f.readline().strip())
                cake.append(derp)
            #finished reading input file for this case
            # Need to make a list of the squares we are dealing with
            zones = [] # store tuples [char,startRow,startCol,width,height]
            
            for row in range(R):
                for col in range(C):
                    # get this character
                    if cake[row][col] != '?':
                        # this is an initial area
                        zones.append([cake[row][col],row,col,1,1,True,True,True,True])
                        
            # Now loop until they are full
            iterNextZone = itertools.cycle(iter(zones))
            z = next(iterNextZone)
            numDirections = len(zones)*4
            while numDirections > 0:
                if case == 41:
                    print(numDirections)
                    print('\n'.join([' '.join(row) for row in cake]))
                    print(''.join(['-']*(2*C-1)))
                    print('Checking zone ' + str(z))
                # check the next zone and see if we can expand it in any direction
                if sum([z[3]*z[4] for z in zones]) == R*C:
                    print('zones are full')
                    break
                # try expanding z up
                if z[5]:
                    if z[1] > 0:
                        for col in range(z[2],z[2]+z[4]):
                            # for each column, check the cell above
                            if cake[z[1]-1][col] != '?':
                                z[5] = False # Don't bother checking up for this zone anymore
                                numDirections = numDirections - 1                            
                                break
                        else:
                            # no blockers found, expand!
                            for col in range(z[2],z[2]+z[4]):
                                # for each column, write the cell above
                                cake[z[1]-1][col] = z[0]
                            # update the zone data
                            z[1] = z[1]-1
                            z[3] = z[3]+1
                    else:
                        z[5] = False # Don't bother checking up for this zone anymore
                        numDirections = numDirections - 1   
                # next try expanding z left
                elif z[6]:
                    if z[2] > 0:
                        for row in range(z[1],z[1]+z[3]):
                            # for each column, check the cell to the left
                            if cake[row][z[2]-1] != '?':
                                z[6] = False
                                numDirections = numDirections - 1                            
                                break
                        else:
                            # no blockers found, expand!
                            for row in range(z[1],z[1]+z[3]):
                                # for each column, write the cell above
                                cake[row][z[2]-1] = z[0]
                            # update the zone data
                            z[2] = z[2]-1
                            z[4] = z[4]+1
                    else:
                        z[6] = False
                        numDirections = numDirections - 1
                # next try expanding right
                elif z[8]:
                    if z[2]+z[4] < C:
                        for row in range(z[1],z[1]+z[3]):
                            # for each column, check the cell to the left
                            if cake[row][z[2]+z[4]] != '?':
                                z[8] = False
                                numDirections = numDirections - 1                            
                                break
                        else:
                            # no blockers found, expand!
                            for row in range(z[1],z[1]+z[3]):
                                # for each column, write the cell above
                                cake[row][z[2]+z[4]] = z[0]
                            # update the zone data
                            z[4] = z[4]+1
                    else:
                        z[8] = False
                        numDirections = numDirections - 1
                # next try expanding down
                elif z[7]:
                    if z[1]+z[3] < R:
                        for col in range(z[2],z[2]+z[4]):
                            # for each column, check the cell above
                            if cake[z[1]+z[3]][col] != '?':
                                z[7] = False
                                numDirections = numDirections - 1                            
                                break
                        else:
                            # no blockers found, expand!
                            for col in range(z[2],z[2]+z[4]):
                                # for each column, write the cell above
                                cake[z[1]+z[3]][col] = z[0]
                            # update the zone data
                            z[3] = z[3]+1
                    else:
                        z[7] = False
                        numDirections = numDirections - 1
                else:
                    z = next(iterNextZone)
                
            o.write('Case #{}:\n{}\n'.format(case,'\n'.join([''.join(row) for row in cake])))
print('done')
                