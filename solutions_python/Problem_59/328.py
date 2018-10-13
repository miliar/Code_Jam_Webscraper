#!/usr/bin/python

#fi = open("A-test.in", "r")
#fi = open("A-small-attempt0.in", "r")
fi = open("A-large.in", "r")
#fi = open("A-large-practice.in", "r")
#fo = open("A-test.out", "w")
#fo = open("A-small-attempt0.out", "w")
fo = open("A-large.out", "w")
#fo = open("A-large-practice.out", "w")

T = int(fi.readline().strip())

for Cases in xrange(1,T+1):

  N,K=fi.readline().strip().split()

#  print N,K

  tree={}

  path1=[]
  path2=[]

  for i in xrange(int(N)):
    path1.append(fi.readline().strip().split('/'))
#    print path1
#    for j in xrange(1,len(path)):
#      if path[j] not in tree:
  A={}
  for i in xrange(int(N)):
    A=tree
    for j in xrange(1,len(path1[i])):
      if path1[i][j] not in A:
        A[path1[i][j]]={}
      A=A[path1[i][j]]

  for i in xrange(int(K)):
    path2.append(fi.readline().strip().split('/'))
#    print path2
  
  mkdir=0

  for i in xrange(int(K)):
    A=tree
    for j in xrange(1,len(path2[i])):
      if path2[i][j] not in A:
	mkdir+=1
        A[path2[i][j]]={}
      A=A[path2[i][j]]

#  print tree

  print 'Case #%d: %d' % (Cases, mkdir)
  fo.writelines('Case #%d: %d\n' % (Cases, mkdir))

fi.close()
fo.close()
