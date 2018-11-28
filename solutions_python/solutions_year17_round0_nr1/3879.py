
# codejam problem A
# python 3
# dariox@gmail.com


import random

def flip(pklist, flp, r):

  for i in range(r, r+flp):
    if (pklist[i]=="+"):
      pklist[i]="-"
    else:
      pklist[i]="+"

  return



def solve(cn, pkc, flp):

  print("Case #", end="")
  print(str(cn), end=": ")

  pklist=list(pkc)
  plen=len(pklist)

  cnt=0
  mne=0
  while ("-" in pklist):
    cnt=cnt+1
    r=0
    while (pklist[r]!="-"):
      r=r+1
    if (r>plen-flp):
      print("IMPOSSIBLE")
      return
    flip(pklist, flp, r)

  print(cnt)
  return



nl = int(input())  # read a line with a single integer
for cn in range(1, nl+1):
  pkc, flp=input().split(" ")
  flp=int(flp)

  solve(cn, pkc, flp)

