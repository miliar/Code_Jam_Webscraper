#!/usr/bin/env python
import sys

def cal(seq):
    seq = [int(i) for i in seq]
    ls = seq[:]
    ls.sort()
    rs = map(lambda a,b:a==b, seq, ls)
    return rs.count(False)

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
        l = f.readline()
        inputs.append(l)
        l = f.readline()
        inputs.append(l)
    return inputs
   
if __name__=='__main__':
    inputs = rf(sys.argv[-1])
    #inputs = ['2','2 1']
    #inputs = ['3','1 3 2']
    #inputs = ['4', '2 1 4 3']
    #inputs = ['2', '1 2']
    print inputs

    results = []
    for i,ip in enumerate(inputs):
        if not i%2:
            continue
        print i,ip
        seq = ip.split()
        rt = cal(seq)
        results.append('%6f'%rt)
    wf(sys.argv[-1][:-2]+'out',results)

