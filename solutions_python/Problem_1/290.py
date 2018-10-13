import sys
import math
import os, os.path
from file_access import open_file, cnum



def problem_testcase(fin, fout, t):
    S = int(fin.readline().strip())
    Sl = [ fin.readline().strip() for i in range(S)]
    #print S
    print Sl
        
    Q = int(fin.readline().strip())
    Ql = [ fin.readline().strip() for i in range(Q)]
    
    #print Q
    print Ql

    start = 0
    stop = False
    nextpos = [0]*S
    switches = 0
    wayoff= 100000000
    while True:
        for i,s in enumerate(Sl):
            try:
                nextpos[i] = Ql.index(s, start)
                print nextpos[i],
            except ValueError:
                nextpos[i] = wayoff
        print
        
        nexts = max(nextpos)
        
        print nexts
        if nexts< Q:
            print Ql[nexts]
        if nexts == wayoff:
            break
        switches += 1
        start = nexts
    print switches
    return [switches]










    
if __name__=='__main__':
    open_file(__file__)
    
    
    

    

