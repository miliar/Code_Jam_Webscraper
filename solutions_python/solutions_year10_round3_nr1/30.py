# -*- coding: utf-8 -*-
fname = "A-large"
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
  N = gcj_read()
  wires = []
  intersects = 0
  for wireno in range(N):
    A, B = gcj_read()
    for Ai, Bi in wires:
      if (Ai < A and Bi > B) or (Ai > A and Bi < B):
	intersects += 1
    wires.append((A, B))
  fout.write("Case #"+str(caseno+1)+": "+ str(intersects) +"\n")

fin.close()
fout.close()