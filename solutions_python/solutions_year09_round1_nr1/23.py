import sys
from numpy import *

import pickle

def ReadInt():
  return int(sys.stdin.readline())

def ReadInts():
  return map(int,sys.stdin.readline().split())

lim = 100000

def MakeTrans():
  BTabs = {}
  for base in xrange(2,11):
    table = zeros(lim,'i')
    for num in xrange(1,lim):
      next = 0
      cur = num
      while cur>0:
        x = cur%base
        next += x*x
        cur /= base
      table[num] = next
    BTabs[base] = table
  return BTabs

def MakeHappy(BTabs):
  Happysets = {}
  for base in xrange(2,11):
    Happy = set([1])
    table = BTabs[base]
    isHappy = zeros(lim)
    isHappy[1]=1
    new = 1
    while new!=0:
      new = 0
      for num in xrange(1,lim):
        if isHappy[num]==0:
          if table[num] in Happy:
            Happy.add(num)
            isHappy[num]=1
            new+=1
    Happysets[base]=Happy
  return Happysets

#file = open("happy.pickle",'w')
#pickle.dump(MakeHappy(MakeTrans()),file)

file = open("happy.pickle",'r')
Happysets = pickle.load(file)

N = ReadInt()

for case in xrange(1,N+1):
  bases = ReadInts()
  S = Happysets[bases[0]]
  for b in bases:
    S = S & Happysets[b]
  L = list(S)
  L.sort()
  n = L[1]
  print "Case #%s: %s"%(case,n)