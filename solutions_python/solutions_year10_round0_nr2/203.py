
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


def calgcd(n,m):
    if n==m:
        return n
    if n<m:
        v=n
        n=m
        m=v
    res=n%m
    if not res==0:
        return calgcd(m,res)
    else:
        return m



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
    ar=mat[i+1]
    n=ar[0]
    assert len(ar)==n+1
    print('Case #'+str(i+1))
    stack=[]
    for j in range(1, len(ar)):
        stack.append(int(ar[j]))
    stack.sort()
    print('stack')
    print(stack)
    diff=[]
    for j in range(0, len(stack)-1):
#        assert stack[j+1]>stack[j]
        if stack[j+1]>stack[j]:
            diff.append(stack[j+1]-stack[j])
    
    diff.sort()
    print('diff')
    print(diff)

    #now calculate GCD for these diff
    if len(diff)==1:
        gcd=diff[0]
    else:
        gcd=diff[0]
        for j in range(1, len(diff)):
            gcd= calgcd(gcd,diff[j])

    res=stack[0]%gcd
    print('gcd')
    print(gcd)
    print('res')
    print(res)
    if res==0:
        time=0
    else:
        time=gcd-res

    line = 'Case #'+str(i+1)+': '+str(time)+'\n'
    of.write(line)




of.close()
