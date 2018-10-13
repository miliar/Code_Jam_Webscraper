import sys
import math
import os
from subprocess import Popen

def main():
    rf = open('C-large.in')
    T = int(rf.readline())
    
    wf = open('C-output' , 'w')
    for i in xrange(T):
        N = int(rf.readline())
        candy = [int(x) for x in rf.readline().split()]
        xor = 0
        for j in xrange(N):
            xor = xor ^ candy[j]
        if xor:
            wf.write('Case #' + str(i+1) + ': NO\n')
        else:
            candy_sum = 0
            candy_min = candy[0]
            for j in xrange(N):
                candy_sum += candy[j]
                if (candy[j] < candy_min):
                    candy_min = candy[j]
                    
            wf.write('Case #' + str(i+1) + ': ' + str(candy_sum - candy_min) + '\n')
            
    rf.close()
    wf.close()

if __name__ == '__main__':
    main()
