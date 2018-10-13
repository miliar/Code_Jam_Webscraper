# -*- coding: utf-8 -*-
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
  N, K, B, T = gcj_read()
  B = float(B)
  X = gcj_read()
  if type(X) != list:
    X = [X]
  V = gcj_read()
  if type(V) != list:
    V = [V]
  Y = [[0.0] for i in range(N)]
  chickens = zip(X, V, Y)
  #Natural speed
  runbydeadline = 0
  for start, speed, time in chickens:
    time[0] = (B-start)/speed
    if time[0] <= T:
      runbydeadline += 1
  print K, runbydeadline
  print chickens
  if runbydeadline < K:
    fout.write("Case #"+str(caseno+1)+": IMPOSSIBLE\n")
    print caseno+1, "IMPOSSIBLE"
    continue
      
  simplyintime = 0
  reqmovesperchicken = []
  for i in reversed(range(N-1)):
    thisctime = chickens[i][2][0]
    if thisctime <= T:
      reqmoves = 0
      for chicken in chickens[i+1:]:
	time = chicken[2][0]
	if time > T:
	  reqmoves += 1
      reqmovesperchicken.append(reqmoves)
  if chickens[-1][2][0] <= T:
    reqmovesperchicken.append(0)

  #print chickens
  print reqmovesperchicken
  reqmovesperchicken.sort()
  totalmoves = sum(reqmovesperchicken[:K])
  fout.write("Case #"+str(caseno+1)+": "+ str(totalmoves) +"\n")

fin.close()
fout.close()