#!/usr/bin/env python

fin = open("B-large.in.txt")
#fin = open("B-small-attempt0.in.txt")
#fin = open("sampleinput.txt")
fout = open("B-large.out.txt", "w")
#fout = open("B-small-attempt0.out.txt", "w")
#fout = open("sampleoutput.txt", "w")

T = int(fin.readline().strip())
for X in range(1,T+1):
  line = fin.readline()
  N, S, p, string = line.strip().split(" ", 3)
  N, S, p = int(N), int(S), int(p)
  totalscore = map(int, string.strip().split(" "))

  if N != len(totalscore):
    print "Error!"

  nY = 0 # counter for NONSURPRISING qualifying triplets
  sY = 0 # counter for SURPRISING qualifying triplets
  for j in range(0, N):
    # compute the most even set of three scores for each total score
    if totalscore[j] >= p + max(0,p-1) + max(0,p-1):
      nY = nY+1
    elif totalscore[j] >= p + max(0,p-2) + max(0,p-2):
      sY = sY+1

  if sY > S:
    sY = S

  fout.write("Case #" + str(X) + ": " + str(nY+sY) + "\n")

fin.close()
fout.close()
