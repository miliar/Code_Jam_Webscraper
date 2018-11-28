#!/usr/bin/python

import sys,re

if len(sys.argv) != 2:
  print "usage: " + sys.argv[0] + " infile"
  sys.exit()
infile = sys.argv[1]

maxcases = 0
linenum = 0
casenum = 0

def onecase(line):
  tokens = line.split()
  i = 0
  combines = {}
  opposers = []
  for j in range(i + 1, int(tokens[0]) + 1):
    i = i + 1
    combines[tokens[j][0:2]] = tokens[j][2]
    combines[tokens[j][1::-1]] = tokens[j][2]
  i = i + 1
  for j in range(i + 1, int(tokens[i]) + i + 1):
    i = i + 1
    opposers.append(tokens[j])
    opposers.append(tokens[j][::-1])
  i = i + 1
  instring = tokens[i + 1]
  output = []
  for char in instring:
    output.append(char)
    output = trycombines(output, combines)
    output = tryopposers(output, opposers)
  return getoutputstr(output)


def trycombines(output, combines):
  if len(output) < 2: return output
  key = output[-1] + output[-2]
  if not key in combines: return output
  val = combines[key]
  output.pop()
  output[-1] = val
  return output


def tryopposers(output, opposers):
  for item in output[:-1]:
    key = item + output[-1]
    if key in opposers: return []
  return output


def getoutputstr(output):
  if len(output) == 0: return "[]"
  str = "["
  for item in output:
    str = str + item + ", "
  str = str[:-2] + "]"
  return str


indata = open(infile, 'r').read().split('\n')
for line in indata:
  linenum = linenum + 1
  if linenum == 1:
    maxcases = int(line)
    continue
  casenum = casenum + 1
  if casenum > maxcases:
    break

  result = onecase(line)
  print "Case #" + str(casenum) + ": " + result





