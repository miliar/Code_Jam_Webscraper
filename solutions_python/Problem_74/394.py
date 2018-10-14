import sys
import math
import os
from subprocess import Popen

def main():
    rf = open('A-large.in')
    wf = open('smalloutput', 'w')
    T = int(rf.readline())
    
    for j in xrange(T):
        problem = rf.readline().split()
        N = int(problem[0])
        print N
        
        last_b = 0
        last_o = 0
        ans = 0
        curr_o = 1
        curr_b = 1
        
        for i in xrange(N):
            if problem[2*i + 1] == 'O':
                diff = math.fabs(int(problem[2*i + 2]) - curr_o)
                if diff >= last_b:
                    last_o += (diff - last_b + 1)
                    ans += (diff - last_b + 1)
                else:
                    last_o += 1
                    ans += 1
                last_b = 0                    
                curr_o = int(problem[2*i + 2])
            else:
                diff = math.fabs(int(problem[2*i + 2]) - curr_b)
                if diff >= last_o:
                    last_b += (diff - last_o + 1)
                    ans += (diff - last_o + 1)
                else:
                    last_b += 1
                    ans += 1
                last_o = 0
                curr_b = int(problem[2*i + 2])
                
        wf.write('Case #' + str(j+1) + ': ' + str(int(ans)) + '\n')

        

if __name__ == '__main__':
    main()
