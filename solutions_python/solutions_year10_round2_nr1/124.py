
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
        value = int(item)
        row.append(value)
      result.append(row)
  return result



if len(sys.argv)<2:
  print('input file needed')
  sys.exit()

fname=sys.argv[1]
print(fname)

fin=fileinput.input(fname)
line=fin[0]

ncases = int(line)

print(ncases)

outfname='out.txt'
of = open(outfname, 'w')


currow=1
for i in range(0, ncases):
    print('Case #'+str(i+1))
    line = fin[currow]
    print(line[0:len(line)-1])
    ar=line.split()

    N=int(ar[0])
    M=int(ar[1])
    assert N>=0 and M>=0
    currow+=1

    edirs=[]
    for j in range(0, N):
        line=fin[currow+j]
        assert len(line)>0
        if line[len(line)-1]=='\n':
            line=line[0:len(line)-1]
        edirs.append(line)
    currow+=N
    ndirs=[]
    for j in range(0, M):
        line=fin[currow+j]
        assert len(line)>0
        if line[len(line)-1]=='\n':
            line=line[0:len(line)-1]
        ndirs.append(line)
    currow+=M

    print(edirs)
    print(ndirs)

    dirmap={}
    for dirpath in edirs:
        dirs=dirpath.split('/')
#        print('dirs')
#        print(dirs)
        curmap=dirmap
        for dir in dirs:
            if not len(dir)==0:
#                print(dir)
                if not dir in curmap:
                    curmap[dir]={}
                curmap=curmap[dir]
    print(dirmap)

    cnt=0
    for dirpath in ndirs:
        dirs=dirpath.split('/')
        curmap=dirmap
        for dir in dirs:
            if not len(dir)==0:
                if not dir in curmap:
                    curmap[dir]={}
                    cnt+=1
                curmap=curmap[dir]

    print(dirmap)
    oline = 'Case #'+str(i+1)+': '+str(cnt)
    print(oline)
    oline+='\n'
    of.write(oline)






of.close()
