#!/usr/bin/env python

import sys
import array

def main():
  num_cases = int(sys.stdin.readline().strip())
  for case in range(1,num_cases+1):
    (rs,ks,ns) = sys.stdin.readline().split()
    (r,k,n) = (int(rs), int(ks), int(ns))

    capacity = k;
    groups = sys.stdin.readline().split()
    for i in range(len(groups)):
      groups[i] = int(groups[i]);

    numGroups = len(groups);
    euro = 0
    nextGroup = 0
    for run in range(r): 
      firstGroup = nextGroup
      riders = 0
      # fill up!
      # for single-group case: let first group board before checking if next group is first group!
      while (riders + groups[nextGroup]) <= capacity:
        riders += groups[nextGroup]
 #       print ("\t\tgroup: " + str(groups[nextGroup]));
        nextGroup = (nextGroup +1) % numGroups
        if (nextGroup == firstGroup) :
          break
      euro += riders
#      print ("\tRun riders: " + str(riders));
    
    print ("Case #" + str(case) + ": " + str(euro));

main()
