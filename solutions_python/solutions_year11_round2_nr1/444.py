import sys
import math
import os
from subprocess import Popen

#global debug

def dprint(*args):
    global debug
    if debug:
        for arg in args:
            print args,
        print

def main():
    global debug
    debug = 1
    
    print 'input-file : ',(sys.argv[0])[:-2] + 'in'
    
    rf = open((sys.argv[0])[:-2] + 'in')
    wf = open((sys.argv[0])[:-2] + 'out', 'w')
    
    T = int(rf.readline())
    
    for i in xrange(T):
        N = int(rf.readline())
        lines = []
        owp = [0] * N
        oowp = [0] * N
        rip = [0] * N
        dot_count = [0] * N
        one_count = [0] * N
        wp = []
        for j in xrange(N):
            lines.append(rf.readline().strip())
            one_count[j] = 0
            dot_count[j] = 0
            for k in xrange(N):
                if lines[j][k] == '1':
                    one_count[j] += 1
                elif lines[j][k] == '.':
                    dot_count[j] += 1
            wp.append(float(one_count[j])/(N - dot_count[j]))
            
        for j in xrange(N):#for owp
            owp[j] = 0
            for k in xrange(N):
                if (lines[j][k] == '.'):
                    continue
                    
                if lines[k][j] == '1':
                    owp[j] += (float(one_count[k] - 1) / (N - dot_count[k] - 1))
                elif lines[k][j] == '0':
                    owp[j] += (float(one_count[k]) / (N - dot_count[k] - 1))
            owp[j] = float(owp[j])/(N - dot_count[j])
        
        for j in xrange(N):
            oowp[j] = 0
            for k in xrange(N):
                if lines[j][k] == '.':
                    continue
                oowp[j] += owp[k]
            oowp[j] /= (N - dot_count[j])

        for j in xrange(N):
            rip[j] = 0.25 * wp[j] + 0.50 * owp[j] + 0.25 * oowp[j]
            
        wf.write('Case #' + str(i+1) + ':\n')
        for j in xrange(N):
            wf.write(str(rip[j]) + '\n')
        

if __name__ == '__main__':
    main()
