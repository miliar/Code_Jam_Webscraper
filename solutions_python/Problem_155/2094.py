#!/usr/bin/python3

def processCase(mshy, lvls):
  acc = 0
  add = 0
  for lvl, ns in enumerate(lvls):
    n = int(ns)
    if lvl > acc:
      add += lvl - acc
      acc = lvl
    acc += n
  return add

if __name__ == "__main__":
  cases = int(input())
  for i in range(cases):
    mshy, shynesses = input().split()
    r = processCase(mshy, shynesses)
    print("Case #%d: %d"%(i+1, r))

