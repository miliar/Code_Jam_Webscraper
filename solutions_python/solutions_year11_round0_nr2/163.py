import re
fin  = "B-large.in"
fout = open(fin.replace("in","out"),"w")
finh = open(fin)
T    = int(finh.readline())
els  = "QWERASDF"
for t in range(1,T+1):
  tt   = {} # Transition Table
  dt   = {} # Destruction Table
  data = finh.readline().split(" ")
  C = int(data[0])
  for c in range(1,C+1):
    (a,b,z) = data[c]
    tt.setdefault(a,{})[b] = z
    tt.setdefault(b,{})[a] = z
  D = int(data[1+C])
  for d in range(1,D+1):
    (a,b) = data[C+1+d]
    dt.setdefault(a,[]).append(b)
    dt.setdefault(b,[]).append(a)
  N = int(data[2+C+D])
  s = []
  for ch in data[3+C+D].rstrip():
    s.append(ch)
    if len(s)<=1: continue
    if s[-2] in tt.keys():
      if s[-1] in tt[s[-2]]:
        s[-2] = tt[s[-2]][s[-1]]
        del s[-1]
    if s[-1] in dt.keys():
      for x in dt[s[-1]]:
        if x in s[:-1]: 
          s = []
          continue
  print >>fout,"Case #%d: [%s]" % (t,", ".join(s))
finh.close()
fout.close()
  
