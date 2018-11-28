#!/usr/bin/python
import sys

lines = [l.strip() for l in sys.stdin if l.strip()!='']
T = int(lines[0])
for ca in range(T):
  line = lines[ca+1].split(" ")
  c = int(line[0])
  forms = line[1:c+1]
  mt = {}
  for t in forms:
    mt[t[0:2]] = t[2]
    mt[t[0:2][::-1]] = t[2]
#  print forms, mt
  d = int(line[c+1])
  ops = line[c+2:c+2+d]
  mo = {}
  for op in ops:
    mo[op[0]] = op[1]
    mo[op[1]] = op[0]
  inp = line[3+c+d]
#  print ops, mo

  s = ""
  for c in inp:
#    print "...",c
    s += c
    changed = True
    while changed:
      changed = False
      if len(s)>=2:
        if s[-2:] in mt:
#          print "boom ",s[-2:],"to",mt[s[-2:]]
          s = s[:-2]+mt[s[-2:]]
          changed = True
        elif s[-1] in mo:
          if s[:-1].find(mo[s[-1]])>=0:
#            print "ops ",s[-1],mo[s[-1]]
            s = ""
#    print s

  print "Case #%d: %s" % (ca+1, str([c for c in s]).replace("'",""))

