
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
    line = fin[i+1]

    ar=line.split()

    nc=int(ar[0])

    cdict={}
    for j in range(0, nc):
        cc=ar[j+1]
        assert len(cc)==3
#        print(cc)
        if not cc[0] in cdict:
            scc={}
            cdict[cc[0]]=scc
        cdict[cc[0]][cc[1]]=cc[2]

#    print(cdict)
    nd = int(ar[nc+1])

    ddict={}
    for j in range(0, nd):
        dd=ar[2+nc+j]
        assert len(dd)==2
        if not dd[0] in ddict:
            ddict[dd[0]]=[]
        ddict[dd[0]].append(dd[1])
        if not dd[1] in ddict:
            ddict[dd[1]]=[]
        ddict[dd[1]].append(dd[0])
#        print(ddict)

    ss=ar[2+nc+nd+1]
#    print(ss)

#    if i==5:
#        pdb.set_trace()

    lss=int(ar[2+nc+nd])
    assert lss==len(ss)
    oss=''
    for j in range(0, lss):
        oss = oss + ss[j]
        if len(oss)>=2:
            #check combine
            c1=oss[len(oss)-1]
            c2=oss[len(oss)-2]
            flag=0
            if c1 in cdict:
                if c2 in cdict[c1]:
                    oss=oss[:-2]
                    oss = oss+cdict[c1][c2]
                    flag=1
            if not flag>0:
                if c2 in cdict:
                    if c1 in cdict[c2]:
                        oss=oss[:-2]
                        oss=oss+cdict[c2][c1]
        if len(oss)>=2:
            #check clear
            c1=oss[len(oss)-1]
            c2=oss[len(oss)-2]
            if c1 in ddict:
                for c in ddict[c1]:
                    if c in oss:
                        oss=''

    print(oss)

    line='Case #'+str(i+1)
    line = line +': ['
    for j in range(0, len(oss)):
        line = line + oss[j]
        line = line + ', '
    if len(oss)>0:
        line = line[:-2]
    line = line+']\n'

    of.write(line)



#fin = fileinput.input(fname)
#of = open(ofilename,'w')
