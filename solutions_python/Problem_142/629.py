# -*- coding: utf-8 -*-

from pylab import *
import numpy

infile = open('input.txt', 'r')
outfile = open("task1-output.txt", "w")

numcases = int(infile.readline())

for case in range(0, numcases):
    N = int(infile.readline())
    
    mins = []
    minLine = None
    error = False
    minDiff = None
    for I in range(0, N):
        line = infile.readline()
        
        if (error):
            continue
    
        minstr = ''
        prevc = ''
        diff = []
        counter = 0
        for c in line:
            if (c == '\n'):
                continue
            
            if (c != prevc):
                prevc = c
                minstr = minstr + c
                if (minstr != c):
                    diff.append(counter)
                counter = 0
            else:
                counter += 1
                
        if size(diff) < len(minstr):
            diff.append(counter)

        print('diff', diff)
            
        if minLine == None:
            minLine = minstr
        else:
            if minLine != minstr:
                error = True
            
        if minDiff == None:
            minDiff = copy(diff)
        else:
            if (size(diff) != size(minDiff)):
                error = True
            else:
                for i in range(0, size(diff)):
                    if (diff[i] < minDiff[i]):
                        minDiff[i] = diff[i]
            
        mins.append(diff)

        #print('line', line)
        #print('minstr', minstr, diff, minDiff)
        
    #print('Mindiff', minDiff, mins)    
        
    if error:
        print('Case #',(case+1),': Fegla Won');
        outfile.write('Case #'+str(case+1)+': Fegla Won\n')
    else:
        T = 0
        #print('mins', mins)
        min_s = Infinity
        for i in range(0, size(mins,0)):
            
           s = (sum(abs(array(mins) - array(mins[i]))))
           if (s < min_s):
               print(mins[i])
               min_s = s
                
        s = (sum(abs(array(mins) - array(minDiff))))   

        if (s < min_s):
           print(mins[i])
           min_s = s            
                
        print('Case #',(case+1),': ',min_s)
        outfile.write('Case #'+str(case+1)+': '+str(min_s)+'\n')
        
        

outfile.close()
    

