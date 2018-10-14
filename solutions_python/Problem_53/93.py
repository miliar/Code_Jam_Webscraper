
import os
import fileinput
import math
import pdb
import re
import getopt,sys
import copy



def readMat(filename) :
#  pdb.set_trace()
  result = []
  mfile = fileinput.input(filename)
  for line in mfile :
    ar = line.split()
    if len(ar)>0 :
      row = []
      for item in ar :
        value = float(item)
        row.append(value)
      result.append(row)
  return result


def d2b(n):
     re=[]
     assert n>=0
     nn=int(n)
     if nn==0:
       re=[int(0)]
     while nn!=0:
        m=nn%2
        nn=int(nn/2)
        re.append(m)
     return re

if len(sys.argv)<2:
  print('input file needed')
  sys.exit()

fname=sys.argv[1]
print(fname)

mat=readMat(fname)

assert len(mat)>0

ncases = int(mat[0][0])

print(ncases)

outfname='out.txt'
of = open(outfname, 'w')

assert len(mat)>=(ncases+1)
for i in range(0, ncases):
    assert len(mat[i+1])>1
    n=mat[i+1][0]
    k=mat[i+1][1]

    pp=pow(2,n)
    kr = k%pp
    bb=d2b(kr)

    bfound = False
    print(bb)
    if len(bb)<n:
      line = 'Case #'+str(i+1)+': OFF\n'
      of.write(line)
      print('OFF')
    else:
      for digit in bb:
        if digit==0:
          bfound = True
      if bfound:
        line = 'Case #'+str(i+1)+': OFF\n'
        of.write(line)
        print('OFF')
      else:
        line = 'Case #'+str(i+1)+': ON\n'
        of.write(line)
        print('ON')
    
    




of.close()
