def main():
  T = input()
  for t in xrange(T):
    X,S,R,t0,N = map(int,raw_input().split())
    ws = [map(int,raw_input().split()) for n in xrange(N)]
    tott0 = 0.
    i = 0
    j = len(ws)
    ws.sort()
    if ws[i][0] != 0:
      ws.append([0,ws[i][0],0])
    for i in xrange(1,j):
      if ws[i][0] != ws[i-1][1]:
        ws.append([ws[i-1][1],ws[i][0],0])
    if ws[j-1][1] != X:
      ws.append([ws[j-1][1],X,0])
    ws.sort(key=lambda x:x[2])
    tot = 0.
    for w in ws:
      if tott0 < t0:
        tmp = float(w[1]-w[0])/(R+w[2])
        if tott0 + tmp <= t0:
          tott0 += tmp
          tot += tmp
        else:
          tmp = float(R+w[2])*(t0-tott0)
          tot += t0-tott0
          tott0 = t0
          tot += float(w[1]-w[0]-tmp)/(S+w[2])
      else:
        tot += float(w[1]-w[0])/(S+w[2])

    print "Case #%d:"%(t+1),
    print "%.9f"%(tot)
main()
