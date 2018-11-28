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

def add_dirs(tree, subdirs):
  if not subdirs:
    return 0
  numadded = 0
  if not subdirs[0] in tree:
    tree[subdirs[0]] = {}
    numadded += 1
  return add_dirs(tree[subdirs[0]], subdirs[1:]) + numadded

for caseno in range(numcases):
  N, M = gcj_read()
  dirsexisting = {}
  for i in range(N):
    existingdir = fin.readline().strip()
    add_dirs(dirsexisting, existingdir.split("/")[1:])
  print dirsexisting
  totaladded = 0
  for i in range(M):
    newdir = fin.readline().strip()
    totaladded += add_dirs(dirsexisting, newdir.split("/")[1:])
  fout.write("Case #"+str(caseno+1)+": "+ str(totaladded) +"\n")
  
fin.close()
fout.close()