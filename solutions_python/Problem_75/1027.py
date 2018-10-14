#!/usr/bin/python

import sys

fp = open(sys.argv[1],"r")
T = int(fp.readline())

# magicka
# rules of the game:
# combination to be done first
# opposition clears the list

for i in range(T): # for all cases
  comb = []
  comb_res = []
  oppo = {}
  a = fp.readline().split()
  C = int(a[0]) # amount of combinations
  for j in range(C):
    comb.append(a[j+1][0:2])
    comb_res.append(a[j+1][2])
  D = int(a[C+1]) # amount of oppositions
  for j in range(D):
    oppo[(a[C+j+2][0])]=a[C+j+2][1]
    oppo[(a[C+j+2][1])]=a[C+j+2][0] # hashmap of oppositions
  N = int(a[C+D+2]) # amount of cards played
  out = []
#  print comb
#  print oppo
  for j in range(N):
    c = a[C+D+3][j] # invoke card c
#    print "card "+c+" "+str(out)
    combined = False
    if len(out)>0:
      for k in range(len(comb)): # check all combinations
        if (out[-1]==comb[k][0] and c==comb[k][1]) or (out[-1]==comb[k][1] and c==comb[k][0]): # must do a combination
          out[-1] = comb_res[k] # last element gets substituted
          combined = True
          break
    if not combined:
      if c in oppo and oppo[c] in out: # there is an opposition
        out = [] # zero out the list
      else:
        out.append(c) # this can be added
  if len(out) == 0:
    sout = "[]"
  else:
    sout = "["
    for j in range(len(out)):
      if j+1 < len(out):
        sout += out[j]+", "
      else:
        sout += out[j]+"]"
  print "Case #"+str(i+1)+": "+sout
