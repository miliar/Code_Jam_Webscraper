
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

mat=readMat(fname)

assert len(mat)>0

ncases = int(mat[0][0])

print(ncases)

outfname='out.txt'
of = open(outfname, 'w')

assert len(mat)>=(ncases+1)
for i in range(0, ncases):
    oline='Case #'+str(i+1)+': '
    print(oline)

    vec=mat[i*3+1]
    assert len(vec)>3
    N=vec[0]
    K=vec[1]
    B=vec[2]
    T=vec[3]
    X=mat[i*3+2]
    V=mat[i*3+3]
    print('B:'+str(B))
    print('T:'+str(T))
    print('K:'+str(K))

    assert len(X)==N and len(V)==N
    print(X)
    print(V)
    tarrive=[]
    block=N*[False]
    for j in range(0, N):
        x=X[j]
        v=V[j]
        assert B>=x
        dist=B-x
        t=dist/v
        tarrive.append(t)
        block[j]=t>T

    npass=[]
    nblock=[]
    for j in range(0, N):
        cnt=0
        blockcnt=0
        for k in range(j+1, N):
            if tarrive[k]>tarrive[j]:
                #switch needed
                cnt += 1
            if block[k]:
                blockcnt+=1
        npass.append(cnt)
        nblock.append(blockcnt)

    #count possible arriving chicks
    cnt = 0
    for j in range(0, N):
        if (tarrive[j]<=T):
            cnt += 1

    print('tarrive')
    print(tarrive)
    if cnt<K:
        print(oline+'IMPOSSIBLE')
        of.write(oline+'IMPOSSIBLE\n')
    else:
        print('npass')
        print(npass)
        print('nblock')
        print(nblock)
        assert K<=N

        switchcnt=0
        chickcnt=0
        for j in range(0, N):
            curidx=N-1-j
            t=tarrive[curidx]
            if t<=T and chickcnt<K:
                chickcnt+=1
                switchcnt+=nblock[curidx]

        print(oline+str(switchcnt))
        of.write(oline+str(switchcnt)+'\n')








of.close()
