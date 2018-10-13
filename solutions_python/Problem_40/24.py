#!/usr/bin/python

import sys, re
from scipy import *



def main():
    NN = int(sys.stdin.next())
    for nn in range(1,NN+1):
        print 'Case #%d:' % nn
        calculate()
    

def calculate():
    L = int(sys.stdin.next())
    s = []
    for line in range(L):
        s += sys.stdin.next()
    s = re.sub('\(', ' ( ', ''.join(s))
    s = re.sub('\)', ' ) ', s)
    s = s.split()
#    print s
    
    c = root = {'parent':None, 'child':[]}
    i = 0
    while i<len(s):
        if s[i] not in ['(',')']:
            raise Exception()
        if s[i]=='(':
            i+=1
            c_ = {'parent': c, 'value': float(s[i]), 'child':[]}
            i+=1
            if s[i] != ')':
                c_['label'] = s[i]
                i+=1
            c['child'].append( c_ )
            c = c_
        if s[i]==')':
            i+=1
            c = c['parent']

    assert(c == root)
    root = root['child'][0]

            
    A = int(sys.stdin.next())
    for line in range(A):
        s = sys.stdin.next().split()[2:]

        c = root
        p = c['value']
        while 'label' in c:
            if c['label'] in s:
                c = c['child'][0]
                p *= c['value']
            else:
                c = c['child'][1]
                p *= c['value']
        print p
#        print '%0.9f' % p
            
    
    


#         m = re.match('(\d+) (\d+)', sys.stdin.next())
#         (na, nb) = map(int, m.groups())


    
if __name__ == "__main__":
    main()
