
import os
import fileinput
import math
import pdb
import re
import getopt,sys
import copy



def readMat(filename) :
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

def trimString(s) :
    l = len(s)
    assert l>0
    outs=[]
    curc=''
#    pdb.set_trace()
    for i in range(0,l):
        c = s[i]
        if c == 'A' or c == 'B' or c == 'C':
            if not c==curc:
                curc=c
                outs.append(c)

    return outs


if len(sys.argv)<2:
  print('usage: 022.py input output')
  sys.exit()

fname = sys.argv[1]
if len(sys.argv)<3:
    ofname='output.txt'
else:
    ofname = sys.argv[2]

fin = fileinput.input(fname)
of = open(ofname,'w')

line=fin[0]

ntc=int(line)

assert ntc>0

for i in range(0, ntc):
    nc = int(fin[i*2+1])
    line = fin[i*2+2]

    ar=line.split()

#    print(nc)
    assert len(ar)==nc

    bcandy=[]
    dcandy=[]
    mlcandy=0
    for j in range(0, nc):
        cand=int(ar[j])
        bcand=bin(cand)
        bcand=bcand[2:]
        mlcandy=max(mlcandy, len(bcand))
        dcandy.append(cand)
        bcandy.append(bcand)
    
    for j in range(0, nc):
        scandy=bcandy[j]
        ncandy=mlcandy*[0]
        offset=mlcandy-len(scandy)
        for k in range(0, len(scandy)):
            ncandy[k+offset]=int(scandy[k])
        bcandy[j]=ncandy

    cnta=mlcandy*[0]

    for j in range(0, nc):
        ncandy=bcandy[j]
        for k in range(0, mlcandy):
            cnta[k] = cnta[k] + ncandy[k]
    s=0
    for j in range(0, mlcandy):
        cnta[j] = cnta[j]%2
        s += cnta[j]
    
    if s>0:
        line = 'Case #'+ str(i+1)+': NO\n'
    else:
        candymin=dcandy[0]
        total=0
        for j in range(0, nc):
            c=dcandy[j]
            candymin=min(candymin, c)
            total += c
        result=total-candymin
        line = 'Case #'+ str(i+1)+': ' + str(result) + '\n'

    of.write(line)
    print(line)

    


#fin = fileinput.input(fname)
#of = open(ofilename,'w')
