import sys

ifname,ofname = sys.argv[1:3]

def recycle(s,i):
  return s[i:] + s[0:i]

ifile = open (ifname,'r')
ofile = open (ofname,'w')

nl = 0
for i,ln in enumerate (ifile):
  if i == 0: 
    nl = int(ln.strip())
    continue
  if i > nl:
    break
  stra,strb = ln.strip().split()
  a,b = int(stra),int(strb)  
  nd = len(stra)
  tot = 0
  for n in range(a,b):
    seen = []
    strn = str(n)
    for j in range(1,nd):
      m = int(recycle(strn,j))
      if m<=n or m>b: continue
      temp = (n,m)
      if temp not in seen: 
        seen += [temp]
        tot += 1
  ofile.write("Case #%d: %d\n" % (i,tot))
ifile.close()
ofile.close()
