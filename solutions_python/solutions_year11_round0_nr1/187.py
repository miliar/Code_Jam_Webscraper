
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
  print('usage: 01.py input output')
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
    line = fin[i+1]

    ar=line.split()

    assert len(ar)%2==1

    nbtn=int(ar[0])
    lb=0
    lo=0
    lbp=1
    lop=1
    flag=0 # color of last button >0 blue <0 orange
    for j in range(0, nbtn):
        color=ar[j*2+1]
        pos=int(ar[j*2+2])
                
#        if j==3 and i == 0:
#            pdb.set_trace()
        if color=='B':
            if flag>=0:
                #still blue or first move
                lb = lb + abs(pos-lbp) + 1
            else:
                lb = max(lb + abs(pos-lbp) + 1, lo+1)
            flag = 1
            lbp=pos
        elif color=='O':
            if flag<=0:
                #still blue or first move
                lo = lo + abs(pos-lop) + 1
            else:
                lo = max(lo + abs(pos-lop) + 1, lb+1)
            flag = -1
            lop=pos
#        print(str(lb)+':'+str(lo))

    print('answer:'+str(max(lb, lo)))

    caseno=i+1
    line = 'Case #'+str(caseno)+': ' + str(max(lb,lo))+'\n'
    of.write(line)

#fin = fileinput.input(fname)
#of = open(ofilename,'w')
