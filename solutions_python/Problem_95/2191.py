#!/usr/bin/python -u

import sys,re

if len(sys.argv) != 2:
  print "usage: " + sys.argv[0] + " infile"
  sys.exit()
infile = open(sys.argv[1], 'r')

debugprint = 0

def convertletter(letter):
  if(letter == 'a'):
    return 'y'
  if(letter == 'b'):
    return 'h'
  if(letter == 'c'):
    return 'e'
  if(letter == 'd'):
    return 's'
  if(letter == 'e'):
    return 'o'
  if(letter == 'f'):
    return 'c'
  if(letter == 'g'):
    return 'v'
  if(letter == 'h'):
    return 'x'
  if(letter == 'i'):
    return 'd'
  if(letter == 'j'):
    return 'u'
  if(letter == 'k'):
    return 'i'
  if(letter == 'l'):
    return 'g'
  if(letter == 'm'):
    return 'l'
  if(letter == 'n'):
    return 'b'
  if(letter == 'o'):
    return 'k'
  if(letter == 'p'):
    return 'r'
  if(letter == 'q'):
    return 'z'
  if(letter == 'r'):
    return 't'
  if(letter == 's'):
    return 'n'
  if(letter == 't'):
    return 'w'
  if(letter == 'u'):
    return 'j'
  if(letter == 'v'):
    return 'p'
  if(letter == 'w'):
    return 'f'
  if(letter == 'x'):
    return 'm'
  if(letter == 'y'):
    return 'a'
  if(letter == 'z'):
    return 'q'
  if(letter == 'A'):
    return 'Y'
  if(letter == 'B'):
    return 'H'
  if(letter == 'C'):
    return 'E'
  if(letter == 'D'):
    return 'S'
  if(letter == 'E'):
    return 'O'
  if(letter == 'F'):
    return 'C'
  if(letter == 'G'):
    return 'V'
  if(letter == 'H'):
    return 'X'
  if(letter == 'I'):
    return 'D'
  if(letter == 'J'):
    return 'U'
  if(letter == 'K'):
    return 'I'
  if(letter == 'L'):
    return 'G'
  if(letter == 'M'):
    return 'L'
  if(letter == 'N'):
    return 'B'
  if(letter == 'O'):
    return 'K'
  if(letter == 'P'):
    return 'R'
  if(letter == 'Q'):
    return 'Z'
  if(letter == 'R'):
    return 'T'
  if(letter == 'S'):
    return 'N'
  if(letter == 'T'):
    return 'W'
  if(letter == 'U'):
    return 'J'
  if(letter == 'V'):
    return 'P'
  if(letter == 'W'):
    return 'F'
  if(letter == 'X'):
    return 'M'
  if(letter == 'Y'):
    return 'A'
  if(letter == 'Z'):
    return 'Q'
  return letter

def debug(str, lvl=5):
  if debugprint > lvl: print "[DEBUG]", str

def handleonecase(line1):
  #TODO
  output = ''
  for c in line1:
    debug(c)
    output += convertletter(c)
  return output

maxcases = 0
casenum = 0

line = infile.readline().strip()
maxcases = int(line)
while line:
  casenum = casenum + 1
  if casenum > maxcases: break
  line1 = infile.readline().strip()
  result = handleonecase(line1)
  print "Case #" + str(casenum) + ": " + str(result)




