# -*- coding: utf-8 -*-
"""
Google Code Jam 2009
Qualification A 
Alien Language
"""

# --- modules ---
import sys

# --- func ---
def str2lst(line):
  lst = []
  bInParent = False
  for i in range(len(line)):
    if line[i] == "(":
      ps = i
      bInParent = True
      continue
    elif line[i] == ")":
      pe = i
      lst.append(line[ps+1:pe])
      bInParent = False
      continue
    elif not bInParent:
      lst.append(line[i])
  return lst

# return list of words that match given letter at given index
def match_datas(lst,letline,idx):
  retlst = []
  for word in lst:
    for letter in letline:
      if word[idx] == letter:
        retlst.append(word)
  return retlst

# --- main ---
# Getting 3 parameters
cases = (sys.stdin.readline()).split()
L = int(cases[0])
D = int(cases[1])
N = int(cases[2])

# Making list of words in the alien language
langlst = []
for i in range(D):
  line = (sys.stdin.readline()).rstrip("\n")
  langlst.append(line)

# check test cases
for i in range(N):
  line = (sys.stdin.readline()).rstrip("\n")
  pattern = str2lst(line)
  # Can't match
  if len(pattern) != L:
    print "Case #"+str(i+1)+":",0
  # count words matching pattern
  tmplst = langlst[:]
  for idx in range(L):
    tmplst = match_datas(tmplst,pattern[idx],idx)
    if tmplst == []:
      break
  # print result
  print "Case #"+str(i+1)+":",len(tmplst)
