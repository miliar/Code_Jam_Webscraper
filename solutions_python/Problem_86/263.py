#!/bin/python
import os, sys

filename = "C-small-attempt0"

def getgcd(a, b):
    while b != 0:
       t = b
       b = a % b
       a = t
    return a

def solve(L, H, freqs):
  for i in xrange(L, H+1):
    divides = True
    for j in freqs:
      if j % i != 0 and i % j != 0:
        divides = False
        break
    if divides:
      return i

def solvebad(L, H, freqs):
  # Now, order all the frequencies from lowest to highest.
  # Calculate the GCD of the highest frequencies, and see if all
  # lower numbers divide it and if it's within range.
  freqs.sort()
  gcd = freqs[-1]
  for index in xrange(len(freqs)-2,-1,-1):
    print "Frequency: %d" % freqs[index]
    gcd = getgcd(gcd, freqs[index])
    print gcd
    if gcd > H:
      continue
    if gcd < L:
      return None
    divides = True
    for i in xrange(0, index):
      if gcd % freqs[i] != 0:
        divides = False
        break
    if divides:
      return gcd
    
infile = open("%s.in" % filename,"rb")
outfile = open("%s.out" % filename, "wb")
T = int(infile.readline())
for index in xrange(T):
  
  N, L, H = map(int,infile.readline().split())
  freqs = map(int,infile.readline().split())
  
  sol = solve(L, H, freqs)
  
  outfile.write("Case #%d: %s\n" % (index+1, 'NO' if sol is None else sol))