# -*- coding: UTF-8 -*-

import os, sys, math, copy
from operator import itemgetter, attrgetter

try:
    file = sys.argv[1]
except Exception as inst:
    print inst, '\n\nSyota avattava tiedosto parametrina!\n\n'
finally:
    file = sys.argv[1]
    fin = open(file, 'r')
    fout = open(file[:-2]+'out', 'w')
    cases = fin.readline()
    print 'Tapauksia ' + cases

    for case in range(0, int(cases)):
    #for case in range(0, 3):
        print ("\nCase " + str(case+1))
        items = fin.readline()[:-1]
        lines1 = sorted(fin.readline()[:-1].split(" "), key=str.lower)
        lines2 = sorted(fin.readline()[:-1].split(" "), key=str.lower)
        #print items
        #print lines1
        #print lines2

        point_war = 0
        point_dwar = 0
        copy = lines2[:]

        #war game:
        for x in xrange(0,len(lines1)):
            played = None
            for y in xrange(0, len(copy)):
                if lines1[x] < copy[y]:
                    played = copy.pop(y)
                    break
            if played == None:
                point_war += 1
                played = copy.pop(0)
            #print lines1[x], played

        #dwar game:
        for x in xrange(0,len(lines1)):
            if lines1[x] > lines2[0]:
                lines2.pop(0)
                point_dwar +=1
            else:
                lines2.pop(len(lines2)-1)



        result = 'Case #'+str(case+1)+': '+str(point_dwar)+' '+str(point_war)+'\n'

        print (result)
        fout.write(result)
        
        '''
        if len(lines)-1 == len(set(lines)):
            lines.sort()
            number = -1
            for x in xrange(0, len(lines)-1):
                if lines[x] == lines[x+1]:
                    #print (lines[x])
                    number = lines[x]
                    break
            print ('Case #'+str(case+1)+': '+ str(number) + '\n')
            fout.write('Case #'+str(case+1)+': '+ str(number) + '\n')
        elif len(lines) == len(set(lines)):
            print ('Case #'+str(case+1)+': Volunteer cheated!\n')
            fout.write('Case #'+str(case+1)+': Volunteer cheated!\n')
        else:
            print ('Case #'+str(case+1)+': Bad magician!\n')
            fout.write('Case #'+str(case+1)+': Bad magician!\n')
        '''

        
    fin.close()
    fout.close()
