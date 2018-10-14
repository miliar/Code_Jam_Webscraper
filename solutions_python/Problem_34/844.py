#!/usr/bin/python
import sys

def read_lines_input(name):
  f = open(name,'r')
  lines = f.read().split('\n')
  f.close()
  return lines

r_lines = read_lines_input

lines = r_lines(sys.argv[1])
wl = int(lines[0].split()[0])
ewsn = int(lines[0].split()[1])
twsn = int(lines[0].split()[2])

exws = []
tws = []

i = 1
for w in range(ewsn):
  exws.append(lines[i])
  i += 1

for w in range(twsn):
  w = []
  for ch in lines[i].split('('):
    if ')' in ch:
      w.append(ch.split(')')[0])
      if ch.split(')')[1] != '':
        w.append(ch.split(')')[1])
    else:
      for c in ch:
        w.append(c)
  tws.append(w)
  i += 1


def get_c_match(inws,cs,cn):
  outws = []
  for c in cs:
    for w in inws:
      if w[cn] == c:
        outws.append(w)
  return outws

#import re

results = []
for w in tws:
  ws = exws
  for cn,c in enumerate(w):
    ws = get_c_match(ws,c,cn)
  results.append(len(ws))

#print tws

for cn,result in enumerate(results):
  print "Case #"+str(cn+1)+": "+str(result)

