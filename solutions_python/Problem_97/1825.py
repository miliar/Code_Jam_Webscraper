#qwertyuiopasdfghjklzxcvbnm
#zfotwajdkrynscvxuigqmephbl

import sys

f = open('C-small-attempt0.in')
t = f.readlines()

t = t[1:]

nr = 1

import itertools

def check(a, b):
  sa = str(a)
  sb = str(b)
  l = len(sa)
  for i in range(1, l):
    if sa[l-i:]+sa[:l-i]==sb:
      return True
  return False

for line in t:
  sys.stdout.write("Case #"+str(nr)+": ")
  ile = 0
  (a,b) = line.split()
  a=int(a)
  b=int(b)
  for k in range(a,b+1):
    for j in range(k+1,b+1):
      if check(k, j):
        ile=ile+1
  print ile
  nr=nr+1

#print pairs