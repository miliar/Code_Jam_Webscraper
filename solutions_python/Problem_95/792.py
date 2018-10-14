#!/usr/bin/python -tt


import sys
import random
import copy





def main():

    sample = 'ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv'
    answer = 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up'

    d = {}

    for i in range(0, len(sample)):
        d[sample[i]] = answer[i]

    d['z'] = 'q'
    d['q'] = 'z'

    print 'dict len = ', len(d)
   
           
    f = open('A-small-attempt0.in')
    out = open('A-small-attempt0.out','w')
    
    testcases = int(f.readline())
    print 'test number = ', testcases
    for tc in range(1, testcases + 1):
        print 'test case #', tc
        line = f.readline()
        line = line.rstrip()

        l = []
        for c in line:
            l.append(d[c])
            
        res = ''.join(l)
        print 'answer: ', res
        
        out.write('Case #'+str(tc)+': '+res+'\n')
            
    f.close()
    out.close()
    


if __name__ == '__main__':
  main()
