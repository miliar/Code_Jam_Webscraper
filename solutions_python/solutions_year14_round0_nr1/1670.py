# -*- coding: utf-8 -*-
"""
Solves the 'Magic Trick' Problem Google Code Jam Qualifications 2014

https://code.google.com/codejam/contest/2974486/dashboard#s=p0



Created on Fri Apr 11 11:27:51 2014

@author: Luca
"""
import numpy as np
import sys
import re

if __name__ == '__main__':

    if len(sys.argv)<2:
        print 'Need to specify an input file'
        exit(1)

    input_file = sys.argv[1]
    output_file =  'magic_trick_output.txt'    
    do_debug = True
    
    try:
      with open(input_file,'r') as f:
        lines = f.readlines()
        T = int(lines[0])
        print 'Solving Magic Trick Problem for T=%d test cases.'%(T)
        data  = []      
        cnt = 1
        for n in range(0,T):
            settings = np.zeros((2,4,4),dtype = np.int)
            answers = []
            for k in range(0,2):
                answers.append(int(lines[cnt]))
                cnt+=1
                for m in range(0,4):
                   settings[k,m,:] = np.array([int(t) for t in lines[cnt].split()],dtype=np.int)
                   cnt +=1
            data.append((settings,answers))       
            if do_debug:
                print 'Test case %d'%(n+1)
                print 'First answer:%d'%(answers[0])
                for m in range(0,4):
                    print ' '.join([str(t) for t in settings[0,m,:]])
                print 'Second answer:%d'%(answers[1])
                for m in range(0,4):
                    print ' '.join([str(t) for t in settings[1,m,:]])
                
    except IOError:
       print 'File %s not found'%input_file
       exit(1)
       
    # Solve the problem      
    solutions = []
    for n in range(0,T):
        settings = data[n][0]
        answers  = data[n][1]
        set1 = set(settings[0,answers[0]-1,:])
        set2 = set(settings[1,answers[1]-1,:])
        its = set1.intersection(set2)
        if len(its) == 0:
            solutions.append('Volunteer cheated!')
        elif len(its) == 1:
            solutions.append(its.pop())
        else:    
            solutions.append('Bad magician!')
            
    try:
      with open(output_file,'w') as f:
          for n in range(0,T):
              f.write('Case #%d: %s\n'%(n+1,solutions[n]))
    except IOError:
       print 'File %s not found'%output_file
       exit(1)