import sys
import math
import os
from subprocess import Popen

def main():
    rf = open('B-large.in')
    T = int(rf.readline())
    
    wf = open('B-output','w')
    
    for i in xrange(T):
        #print 'Case ', i+1
        line = rf.readline().split()
        C = int(line[0])
        combine = dict()
        for j in xrange(C):
            combine[line[j+1][:2]] = line[j+1][2] 
#        #print combine
        D = int(line[C+1])
        oppose = line[C+2 : (C+D+2)]
#        #print oppose
        N = int(line[C + D + 2])
        seq = line[C + D + 3]
        ans = seq[0]
        ans_index = 0
#        #print seq
        for j in range(1, N):
            if ans_index == -1:
                ans = seq[j]
                ans_index += 1
                continue
        
            pair = ans[ans_index] + seq[j]
            try:
                char = combine[pair]
                ans = ans[:ans_index]
                ans_index -= 1
                ans += char
            except:
                pair = seq[j] + ans[ans_index]
                try:
                    char = combine[pair]
                    ans = ans[:ans_index]
                    ans_index -= 1                    
                    ans += char
                except:
                    ans += seq[j]
            
            ans_index += 1
            #print 'ans_i ', ans_index, 'ans ', ans
            for k in xrange(ans_index):
                if (((ans[k] + ans[ans_index]) in oppose) or ((ans[ans_index] + ans[k]) in oppose)):
                    ans = []
                    ans_index = -1
                    break
                    
        output = 'Case #' + str(i + 1) + ': ['
        if ans:
            output += ans[0]
        for j in range(1, len(ans)):
            output += ', '
            output += ans[j]
        output += ']\n'
        wf.write(output)
if __name__ == '__main__':
    main()
