if __name__=="__main__":
  fin  = "D-large.in"
  fout = open(fin.replace("in","out"),"w")
  finh = open(fin)
  T    = int(finh.readline())
  for t in range(1,T+1):
    N  = int(finh.readline())
    ns = [int(x)-1 for x in finh.readline().split(' ')]
    nS = []
    nS.extend(ns)
    nS.sort()
    print >>fout,"Case #%d: %.6f" % (t,len([a for (a,b) in zip(ns,nS) if a!=b]))
  finh.close()
  fout.close()