#!/usr/bin/env python2.6
# Welcome to Code Jam (90101.2)
# A submission by Cortland Klein <me@pixelcort.com>
# 2009-09-02

# import pdb; pdb.set_trace();

import pdb;
import re;

welcome = 'welcome to code jam'


def determineCount(case, welcome, case_offset, welcome_offset, count):
  caseCharacter = case[case_offset]
  welcomeCharacter = welcome[welcome_offset]
  
  areEqual = caseCharacter == welcomeCharacter
  endOfCase = case_offset+1 == len(case)
  endOfWelcome = welcome_offset+1 == len(welcome)
  
  if areEqual and endOfWelcome:
    count = count + 1
  
  if areEqual and not endOfWelcome:
    count = determineCount(case, welcome, case_offset, welcome_offset+1, count)

  if not endOfCase:
    count = determineCount(case, welcome, case_offset+1, welcome_offset, count)
  
  return count

with open('C-small-attempt0.in.txt') as f:
  n = int(f.next())
  
  for i in range(n):
    case = f.next()
    count = determineCount(case, welcome, 0, 0, 0)
    
    # Begin Dragons
    
    # End Dragons
    
    print "Case #" + str(i+1) + ": " + ("%04d" % count)[-4:]
    
    