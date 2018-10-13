import re
import os

output = open('../SnapperLarge.txt','w')

def getint(f):
  return int(f.readline())

def getints(f):
  return [int(x) for x in f.readline().split()]

def parse(file):
  f = open(file)
  n =  getint(f)
  for i in range(n):
    n,k = getints(f)
    snapper(i+1,n,k)
  return

def snapper(case,n,k):
  mod = 1<<n
  x = k%mod
  on= x==mod-1
  if on:
    print >>output,"Case #%d: ON"%case
  else:
    print >>output,"Case #%d: OFF"%case

parse('/Users/sholte/Downloads/A-large.in')
#parse('../test.in')