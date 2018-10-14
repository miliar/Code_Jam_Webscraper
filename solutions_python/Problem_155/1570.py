import numpy as np
import sys
import re
import math

e=open('C:\Users\haki!\Desktop\entrer12.txt','r')
s=open('C:\Users\haki!\Desktop\sorter12.txt','w')
def read_matrice(m):
    return np.array([map(int,e.readline().split()) for i in xrange(m)])
def read_vect(m):
     return np.array(map(int,e.readline().split()))

N=int(e.readline())#number of case
for i in xrange(1,N+1):
    k=e.readline().split()
    mat=map(int,' '.join(k[1]).split())
    print mat
    c=0
    for j in xrange(len(mat)):
        if mat[j]:
           while sum(mat[:j])<j:
              mat[0]+=1
              c+=1
    s.write('Case #%d: %d\n' %(i,c))
    print 'Case #%i: %s\n' % (i,c)
e.close()
s.close()
