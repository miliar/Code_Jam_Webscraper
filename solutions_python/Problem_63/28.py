# -*- coding: utf-8 -*-
from math import log10, log
fname = "B-large"
fin = open(fname+".in","r")
fout = open(fname+".out","w")
def gcj_read():
  linestr = fin.readline().strip()
  linebits = [int(numb) for numb in linestr.split()]
  if len(linebits) == 1:
    return linebits[0]
  else:
    return linebits

numcases = gcj_read()

for caseno in range(numcases):
  L, P, C = gcj_read()
  L = float(L)
  geom_range = log10(P/L)/log10(C)
  if geom_range < 1:
    splits = 0
  else:
    splits = log(geom_range, 2)
  if splits % 1:
    splits = int(splits) + 1
  else:
    splits = int(splits)
  fout.write("Case #"+str(caseno+1)+": "+ str(splits) +"\n")

fin.close()
fout.close()