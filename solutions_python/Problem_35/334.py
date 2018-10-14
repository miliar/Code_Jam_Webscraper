#!/usr/bin/python

import os
import sys
import math

letters = "abcdefghijklmnopqrstuvwxyz"
LETTERS = letters.upper()

def read_input_NN(fn =""):
  fh = open(fn, "r")
  lines = map(lambda x: x.strip(), fh.readlines())
  fh.close()
  goog_N = int(lines[0])
  line_ctr = 1
  mats = []
  for i in range(goog_N):
    [goog_H,goog_W] = map(int, lines[line_ctr].split())
    mat = []
    for line in lines[line_ctr+1:line_ctr+1+goog_H]:
      mat+=[map(int, line.split())]
    line_ctr+=1+goog_H
    mats = mats+[mat]
  return(mats)

def find_sinks(mat=[[1,2],[1,2]]):
  mat_H = len(mat)
  mat_W = len(mat[0])
  mat_s = []
  for i in range(mat_H):
    s_list = []
    for j in range(mat_W):
      sink_i = "S"
      if i-1 >= 0:
        if mat[i-1][j] < mat[i][j]:
          sink_i = "N"
      if i+1 < mat_H:
        if mat[i+1][j] < mat[i][j]:
          sink_i = "N"
      if j-1 >= 0:
        if mat[i][j-1] < mat[i][j]:
          sink_i = "N"
      if j+1 < mat_W:
        if mat[i][j+1] < mat[i][j]:
          sink_i = "N"
      s_list += [sink_i]
    mat_s += [s_list]
  return(mat_s)

def enumerate_sinks(mat=[[1,2],[1,2]]):
  mat_H = len(mat)
  mat_W = len(mat[0])
  mat_s = []
  letter_ctr = 0
  for i in range(mat_H):
    s_list = []
    for j in range(mat_W):
      pos_i = " "
      if mat[i][j]=="S":
        pos_i = LETTERS[letter_ctr]
        letter_ctr+=1
      s_list += [pos_i]
    mat_s += [s_list]
  return(mat_s)

def expand_sinks(mat=[[1,2],[1,2]], sink = [[1,2],[1,2]]):
  #print mat
  #print sink
  mat_H = len(mat)
  mat_W = len(mat[0])
  mat_s = []
  for i in range(mat_H):
    s_list = []
    for j in range(mat_W):
      altitude = 999999
      sink_i = sink[i][j]
      if i-1 >= 0:
        if mat[i-1][j] < mat[i][j] and sink[i][j]==" " and mat[i-1][j] < altitude:
          sink_i = sink[i-1][j]
          altitude = mat[i-1][j]
      if j-1 >= 0:
        if mat[i][j-1] < mat[i][j] and sink[i][j]==" " and mat[i][j-1] < altitude:
          sink_i = sink[i][j-1]
          altitude = mat[i][j-1]
      if j+1 < mat_W:
        if mat[i][j+1] < mat[i][j] and sink[i][j]==" " and mat[i][j+1] < altitude:
          sink_i = sink[i][j+1]
          altitude = mat[i][j+1]
      if i+1 < mat_H:
        if mat[i+1][j] < mat[i][j] and sink[i][j]==" " and mat[i+1][j] < altitude:
          sink_i = sink[i+1][j]
          altitude = mat[i+1][j]
      s_list += [sink_i]
    mat_s += [s_list]
  return(mat_s)


def flatten(x):
    """flatten(sequence) -> list
    http://kogs-www.informatik.uni-hamburg.de/~meine/python_tricks
    Returns a single, flat list which contains all elements retrieved
    from the sequence and all recursively contained sub-sequences
    (iterables).

    Examples:
    >>> [1, 2, [3,4], (5,6)]
    [1, 2, [3, 4], (5, 6)]
    >>> flatten([[[1,2,3], (42,None)], [4,5], [6], 7, MyVector(8,9,10)])
    [1, 2, 3, 42, None, 4, 5, 6, 7, 8, 9, 10]"""
    result = []
    for el in x:
        #if isinstance(el, (list, tuple)):
        if hasattr(el, "__iter__") and not isinstance(el, basestring):
            result.extend(flatten(el))
        else:
            result.append(el)
    return result

def alpha_sinks(mat=[[1,2],[1,2]]):
  mat_H = len(mat)
  mat_W = len(mat[0])
  mat_s = []
  letter_ctr = 0
  d_l = {}
  for i in range(mat_H):
    s_list = []
    for j in range(mat_W):
      pos_i = " "
      #print mat[i][j]
      if mat[i][j] not in d_l.keys():
        d_l[mat[i][j]] = letters[letter_ctr]
        pos_i = letters[letter_ctr]
        letter_ctr+=1
      else:
        pos_i = d_l[mat[i][j]]
      s_list += [pos_i]
    mat_s += [s_list]
  return(mat_s)

def qb(fn="sample"):
  mats = read_input_NN(fn)
  sinks = []
  for mat in mats:
    sinks += [find_sinks(mat)]
  sinks_e = []
  for sink in sinks:
    sinks_e += [enumerate_sinks(sink)]
  sinks_e2 =[]
  for ctr2 in range(len(sinks)):
    sink_e2 = expand_sinks(mats[ctr2],sinks_e[ctr2])
    #print sink_e2
    #for i in sink_e2:
    #  print "".join(i)
    #print "11111111111111111111"
    while " " in flatten(sink_e2):
      sink_e2 = expand_sinks(mats[ctr2],sink_e2)
      #for i in sink_e2:
      #  print "".join(i)
      #print "11111111111111111111"
    sinks_e2 += [sink_e2]
  sinks_e3 = []
  for sink in sinks_e2:
    sinks_e3 += [alpha_sinks(sink)]
    #print alpha_sinks(sink)
  return(sinks_e3)

l1 = qb(fn="B-large.in")
#print l1

#print l1

#for i in l1:
#  for j in i:
#    print " ".join(j)

fh = open("out.txt","w")
for (ctr,sol) in enumerate(l1):
  print >> fh, "Case #"+str(ctr+1)+":"
  for j in sol:
    print >> fh, " ".join(j)

fh.close()
