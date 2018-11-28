import re
import os
from numpy import *
import fractions

outputF = 'Warning.txt'
inputF = '/Users/sholte/Downloads/B-large.in'
#inputF = '../test.in'

output = open(outputF,'w')

def getint(f):
  return int(f.readline())

def getints(f):
  return [int(x) for x in f.readline().split()]

def parse(file):
  f = open(file)
  n =  getint(f)
  for i in range(n):
    ints = getints(f)
    onecase(i+1,ints)
  return

def onecase(case,ints):
  times = array(ints[1:])
  times.sort()
  off = times[1:]-times[0]
  gcd = off[0]
  for x in off[1:]:
    gcd = fractions.gcd(gcd,x)
  left = (-times[0])%gcd
  print gcd,times,left
  print >>output,"Case #%d: %d"%(case,left)

print "Reading:"+inputF
print "Writing:"+outputF
parse(inputF)