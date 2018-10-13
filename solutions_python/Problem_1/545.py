#!/opt/local/bin/python

import sys, string

input_f = open(sys.argv[1],'r')
count = 1

first_line = input_f.readline()
n_pb = string.atoi(first_line)

def find_min(A):
  min = 10000
  for z in range(0, len(A)):
    if A[z] < min:
      min = A[z]
  return min

def find_ind_min(A):
  min = 10000
  ind = 0
  for z in range(0, len(A)):
    if A[z] < min:
      min = A[z]
      ind = z
  return ind

def find_ind_max(A):
  max = -10
  ind = 0
  for z in range(0, len(A)):
    if A[z] > max:
      max = A[z]
      ind = z
  return ind

for i in range(0, n_pb):
  eng = []
  quer = []
  n_engines = string.atoi(input_f.readline())
  count = []
  first_see = []
  switches = 0
  for j in range(0, n_engines):
    eng.append(input_f.readline().rstrip("\n"))
    count.append(0)
    first_see.append(0)
  n_queries = string.atoi(input_f.readline())
  for k in range(0, n_queries):
    quer.append(input_f.readline().rstrip("\n"))
  for word in quer:
    for c in range(0, n_engines):
      if word == eng[c]:
        count[c] = count[c] + 1
        if count[c] == 1:
          first_see[c] = quer.index(word)
  if find_min(count) == 0:
    actual = eng[find_ind_min(count)]
  else:
    actual = eng[find_ind_max(first_see)]
  quer_rest = quer[0:len(quer)]
  l = 0
  while len(quer_rest) > 0:
    word = quer_rest.pop(0)
    count[eng.index(word)] = count[eng.index(word)] - 1
    l = l + 1
    #print "line : " + str(l) + ", actual search engine is : " + actual
    #print word
    if word == actual:
      #print "switch because actual is : " + actual
      for mot in eng:
        if quer_rest.count(mot) == 0:
          first_see[eng.index(mot)] = 10000
        else :
          first_see[eng.index(mot)] = quer_rest.index(mot)
      #print first_see
      switches = switches + 1
      if find_min(count) == 0 and eng[find_ind_min(count)] != actual:
        # shortcuts with an engine no longer used
        #print " ================================= IN THE IF " 
        #print count
        #print "ENG :::::::::::: " + eng[find_ind_min(count)]
        actual = eng[find_ind_min(count)]
        #print "ENG2 :::::::::::: " + eng[find_ind_min(count)]
        #print "ACTUAL :::::::::::: " + actual
      else:
        #print " IN THE ELSE ========================================= " 
        #print count
        first_see[eng.index(word)] = -1
        actual = eng[find_ind_max(first_see)]

  print "Case #" + str(i+1) + ": " + str(switches)

