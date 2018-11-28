import sys

input = sys.stdin

T = int(input.readline())

for t in xrange(T):
  N = int(input.readline())
  scores = [ list(input.readline().strip()) for i in xrange(N)]

  wps = []
  for s in scores:
    ss = [ int(sss) for sss in s if sss != '.' ]
    wps.append(sum(ss)*1.0/len(ss))

  owps = []
  for i,s in enumerate(scores):
    _wps = []
    for _s in scores:
      ss = [ int(sss) for k, sss in enumerate(_s) if sss != '.' and i != k]
      _wps.append(sum(ss)*1.0/len(ss))
    #print '_wps',_wps
      
    opps = [ _wps[j] for j,ss in enumerate(s) if ss != '.']
    owps.append(sum(opps)*1.0/len(opps))

  oowps = []
  for s in scores:
    _oowp = [owps[i] for i, o in enumerate(s) if o != '.']
    oowps.append(sum(_oowp)*1.0/len(_oowp))

  #print wps
  #print owps
  #print oowps


  print 'Case #%d:'%(t+1)
  answer = [ 0.25 * wps[i] + 0.5 * owps[i] + 0.25 * oowps[i] for i in xrange(N)]
  for a in answer:
    print a
