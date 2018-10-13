fin  = "C-large.in"
fout = open(fin.replace("in","out"),"w")
finh = open(fin)
T    = int(finh.readline())
for t in range(1,T+1):
  N  = int(finh.readline())
  ns = [int(x) for x in finh.readline().split(' ')]
  if reduce(lambda x,y: x ^ y, ns)==0:
    print >>fout, "Case #%d: %d" % (t,sum(ns)-min(ns))
  else:
    print >>fout, "Case #%d: NO" % t
fout.close()