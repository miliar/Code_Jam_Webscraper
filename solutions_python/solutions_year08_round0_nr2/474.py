import sys
for i in range(int(sys.stdin.readline())):
  print "Case #"+str(i+1)+":",
  turnaround=int(sys.stdin.readline())
  partenze=sys.stdin.readline().split()
  NA=int(partenze[0])
  NB=int(partenze[1])
  PA=[]
  PB=[]
  for j in range(NA):
    temp=sys.stdin.readline().split()
    PA.append([60*int(temp[l][0:2])+int(temp[l][3:5]) for l in [0,1]])
  da=[k[0] for k in PA]
  da.sort()
  ab=[k[1] for k in PA]
  ab.sort()
  for j in range(NB):
    temp=sys.stdin.readline().split()
    PB.append([60*int(temp[l][0:2])+int(temp[l][3:5]) for l in [0,1]])
  db=[k[0] for k in PB]
  db.sort()
  aa=[k[1] for k in PB]
  aa.sort()
  # treni che partono da a
  tot=len(da)
  for mu in range(len(da)):
    trovato=False
    for nu in range(len(aa)):
      if aa[nu]+turnaround<=da[mu]:
        tot -= 1
        aa.remove(aa[nu])
        trovato = True
      if trovato:
        break
  print tot,
  tot=len(db)
  for mu in range(len(db)):
    trovato=False
    for nu in range(len(ab)):
      if ab[nu]+turnaround<=db[mu]:
        tot -= 1
        ab.remove(ab[nu])
        trovato = True
      if trovato:
        break
  print tot
