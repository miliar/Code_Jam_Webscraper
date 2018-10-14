import sys

T = int(sys.stdin.readline())

## Embarassing poor solution :) - I think I missed the point
for t in xrange(1,T+1):
  seq = sys.stdin.readline().split()[1:]
  Ol=[]
  Bl=[]
  seq2=[]
  seq2.extend(seq)
  for item in seq:
    if item=="O":
      del seq2[0]
      Ol.append(int(seq2[0]))
      del seq2[0]
    if item=="B":
      del seq2[0]
      Bl.append(int(seq2[0]))
      del seq2[0]

  O=1
  B=1
  c=0
  delete=""
  while True:
    if Ol and seq:
      if Ol[0] > O:
        O +=1
      elif Ol[0] < O:
        O -=1
      elif seq[0]=="O":
        delete="O"

    if Bl and seq:
      if Bl[0] > B:
        B +=1
      elif Bl[0] < B:
        B -=1
      elif seq[0]=="B":
	delete="B"

    if delete=="O":
      del seq[0]
      del seq[0]
      del Ol[0]
      delete=""
    if delete=="B":
      del seq[0]
      del seq[0]
      del Bl[0]
      delete=""


    c+=1

    if len(seq)==0:
      break

  print "Case #%i: %i" %(t,c)
