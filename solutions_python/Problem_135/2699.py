#!/usr/bin/env python
#encoding=utf-8

'''
author:     Eric Zhang(snow31450588@gmail.com)
purpose:    Google Code Jam Qualification Round
history:
    2014-04-11  Initial version
'''

import sys
import string

def calc(a1, ls1, a2, ls2):
    result = set(ls1[a1-1]).intersection(ls2[a2-1])
    if not result:
        return 'Volunteer cheated!'
    if len(result)==1:
        return list(result)[0]
    return 'Bad magician!'

def wf(fileName,results):
    f = open(fileName,'w')
    for i,r in enumerate(results):
        f.write('Case #%d: %s\n'%(i+1,r))
    f.close()

def rf(fileName):
    f = open(fileName,'r')
    inputs = []
    n = int(f.readline())
    for i in range(n):
        a1 = int(f.readline().strip())
        ls1 = []
        for _ in range(4):
            l = f.readline().strip().split()
            ls1.append(l)
        a2 = int(f.readline().strip())
        ls2 = []
        for _ in range(4):
            l = f.readline().strip().split()
            ls2.append(l)
        inputs.append((a1, ls1, a2, ls2))
    return inputs

def main(fin, fout):
    results = []
    
    for a1, ls1, a2, ls2 in rf(fin):
        e = calc(a1, ls1, a2, ls2)
        results.append(e)
    
    wf(fout,results)


if __name__=='__main__':
    fin = sys.argv[1]
    fout = sys.argv[1][:-2]+'out'
    main(fin, fout)
    