#!/usr/bin/python

import sys

def patcalc(pile):
  """ patrick calculation of how much a pile of candies is worth"""
  if len(pile) == 1: # just one candy
    return(pile[0])
  elif len(pile) > 1: # more than 1
    return(patsum(pile[0],patcalc(pile[1:]))) # recurse
    

def patsum(a,b):
  abin = bin(a)
  bbin = bin(b)
  if len(abin) < len(bbin):
    tmp = bbin
    bbin = abin
    abin = tmp # swap them, smaller amount of digits in bbin
  j = len(abin)-1 # last character (least significant bit)
  for k in range(len(bbin)-1,1,-1):
    if bbin[k] == '1' and abin[j] == '1': # patrick will forget the remainder
      abin = abin[0:j]+"0"+abin[j+1:] # flip that bit :)
    elif bbin[k] == '1' and abin[j] == '0':
      abin = abin[0:j]+"1"+abin[j+1:] # patrick is summing 1+0=1
    j -= 1
  return(int(abin,2))

# test the patrick sum
# print patsum(5,4)
# print patsum(4,5)
# print patsum(7,9)
# print patsum(50,10)

def allpiles(pile1,pile2,elements): # DFS on the tree of possibilities
  """ will create a tree of all possible assignment for each element to one of the two piles, will return all cases of pile 1, when pile 2 have equal value"""
  if len(elements)==0: # if empty, leaf node
    if patcalc(pile1) == patcalc(pile2):
      if sum(pile1) >= sum(pile2):
        return [pile1]
      else:
        return [pile2]
    else:
      return []
  else: # not empty, we could give this candy to...
    lb = allpiles(pile1+[elements[0]],pile2,elements[1:]) # to Sean
    rb = allpiles(pile1,pile2+[elements[0]],elements[1:]) # to Patrick
    return lb+rb

fp = open(sys.argv[1],"r")
T = int(fp.readline())

for i in range(T): # for all cases
  N = int(fp.readline()) # amount of candies
  candies = map(int,fp.readline().strip().split())
  common_sum_P = allpiles([],[],candies) # list of Patrick possible piles
  if len(common_sum_P) == 0:
    print "Case #"+str(i+1)+": NO"
    continue
  else:  # only according to Patrick sum, the piles have same value, but the best for Sean?
    bestS = max(map(sum,common_sum_P)) # normal sum , Sean can do math :)
    print "Case #"+str(i+1)+": "+str(bestS)
#    print common_sum_P
