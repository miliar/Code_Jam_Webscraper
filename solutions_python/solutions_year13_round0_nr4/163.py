#!/usr/bin/python

import sys
from time import sleep

def debug(N, chesttype, chestkeys, treasures, keys):
  print >> sys.stderr, "chests:", treasures
  print >> sys.stderr, "keys:",
  for i in range(len(keys)):
    if keys[i] > 0:
      print >> sys.stderr, "%dx%d" % (keys[i],i),
  print >> sys.stderr
  # sleep(0.5)

def dorun(N, chesttype, chestkeys, treasures, keys):
  # print >> sys.stderr, "!!"
  # debug(N,chesttype,chestkeys,treasures,keys)

  if N == len(treasures):
    return treasures
  elif max(keys) == 0:
    # print >> sys.stderr, "no keys"
    # print >> sys.stderr
    # debug(N,chesttype,chestkeys,treasures,keys)
    return False

  rkeys = list(keys)
  for i in range(1,N+1):
    if i not in treasures:
      for k in chestkeys[i]:
        rkeys[k] += 1
  skeys = list(rkeys)
  for i in range(1,N+1):
    if i not in treasures:
      for k in chestkeys[i]:
        rkeys[k] -= 1
      t = chesttype[i]
      if rkeys[t] <= 0 or skeys[t] <= 0:
        # print >> sys.stderr, "not possible!"
        # print >> sys.stderr
        # debug(N,chesttype,chestkeys,treasures,keys)
        return False
      skeys[t] -= 1
      for k in chestkeys[i]:
        rkeys[k] += 1

  tried = False
  for i in range(1,N+1):
    if i not in treasures:
      t = chesttype[i]
      if keys[t] > 0:
        tried = True
        # try open this chest
        treasures.append(i)
        keys[t] -= 1
        for k in chestkeys[i]:
          keys[k] += 1

        # print >> sys.stderr, "open",i,"with",t,"and got:",chestkeys[i]
        res = dorun(N,chesttype,chestkeys,treasures,keys)
        if res != False:
          return res
        # print >> sys.stderr, "close",i

        # undo
        for k in chestkeys[i]:
          keys[k] -= 1
        keys[t] += 1
        treasures.pop()

  # if not tried:
  #   print >> sys.stderr, "useless keys"
  #   print >> sys.stderr
  #   debug(N,chesttype,chestkeys,treasures,keys)
  return False

T = int(sys.stdin.readline())
for t in range(T):
  print >> sys.stderr, "Test: %d" % (t+1)
  toks = sys.stdin.readline().strip().split()
  K = int(toks[0])
  N = int(toks[1])

  keys = [0] * 201
  toks = sys.stdin.readline().strip().split()
  for i in range(K):
    k = int(toks[i])
    keys[k] += 1

  chesttype = [0]
  chestkeys = [0]
  for i in range(N):
    toks = sys.stdin.readline().strip().split()
    chesttype.append(int(toks[0]))
    k = int(toks[1])
    ckeys = []
    for j in range(k):
      ckeys.append(int(toks[2+j]))
    chestkeys.append(ckeys)

  # print K,N
  # print keys
  # print chesttype
  # print chestkeys

  res = dorun(N,chesttype,chestkeys,[],keys)

  print "Case #%d:" % (t+1),
  if res == False:
    print "IMPOSSIBLE"
  else:
    s = ""
    for r in res:
      s += str(r) + " "
    print s.strip()

