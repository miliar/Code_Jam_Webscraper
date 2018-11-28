#!/usr/bin/python

import pickle
import sys
import os

def change(l,d):
  o = ""
  for c in l:
    try:
      o = o+d[c]
    except:
      print "can't translate "+c
      o = o+"."
  return o

def updatedic(d,l,t): # dic, line, translation
  i = 0
  for c in t:
    o = l[i]
    d[o] = c
    i=i+1

def filldic(d): # fill missing letters randomly
  # look for , oh, i found it
  d['q'] = 'z'

dic = {' ':' ','a':'y','o':'e','z':'q'}
tr = [] #output translation
if not os.path.exists("dicfile.a"):
  # create new dictionary
  dicfile = open("dicfile.a","w")
  pickle.dump(dic,dicfile)
else:
  dicfile = open("dicfile.a","r")
  dic = pickle.load(dicfile)

print dic

if len(sys.argv) < 2:
  quit()


if len(sys.argv) > 2:
  f2 = open(sys.argv[2],'r') # sample output

f = open(sys.argv[1],'r')  
line = f.readline() #number of test cases
n = int(line)
for line in f:
  if len(sys.argv) > 2: # got f2
    l2 = f2.readline()
    updatedic(dic,line,l2)
  filldic(dic)
  tr.append(change(line,dic))

# save the updated dictionary
dicfile = open("dicfile.a","w")
pickle.dump(dic,dicfile)

# print output
fout = open("fout.txt","w")
for i in range(1,n+1):
  fout.write("Case #"+str(i)+": "+tr[i-1])

