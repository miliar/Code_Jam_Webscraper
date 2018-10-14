import sys

T = int(sys.stdin.readline())

for t in xrange(1,T+1):
  line = sys.stdin.readline().split()
  Cnum = int(line[0])
  C=[]
  for c in range(Cnum):
    C.append(line[c+1])
  line=line[Cnum+1:]
  Dnum = int(line[0])
  D=[]
  for d in range(Dnum):
    D.append(line[d+1])
  input = line[-1]

  Cdict={}
  for i in C:
    Cdict[i[0]+i[1]]=i[-1]
    Cdict[i[1]+i[0]]=i[-1]

  elist = []
  for e in input:
    elist.append(e)
    if len(elist)>=2 and elist[-2]+elist[-1] in Cdict:
      elist=elist[:-2]+[Cdict[elist[-2]+elist[-1]]]
      continue
    for d in D:
      if d[0] in elist and d[1] in elist:
        elist=[]

  s= "Case #%i: %s" %(t,elist)
  print s.replace("'","")
