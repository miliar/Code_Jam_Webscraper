data = [l.strip() for l in open("A-large.in", "r").readlines()]
out = open("A-large.out", "w")  

ncases = int(data.pop(0))
for case in range(ncases):
  x, s, r, t, n = [int(i) for i in data.pop(0).split(' ')]
  corridor = []
  currpos = 0
  for walk in range(n):
    b, e, w = [int(i) for i in data.pop(0).split(' ')]
    if currpos < b:
      runtime = float(b-currpos) / float(r)
      walktime = float(b-currpos) / float(s)
      corridor.append([0, runtime, walktime, currpos, b])
    runtime = float(e-b) / float(r+w)
    walktime = float(e-b) / float(s+w) 
    corridor.append([w, runtime, walktime, b, e])
    currpos = e
  if currpos < x:
    runtime = float(x-currpos) / float(r)
    walktime = float(x-currpos) / float(s)
    corridor.append([0, runtime, walktime, currpos, x])
  corridor.sort()
  totalruntime = t
  totaltime = 0
  while len(corridor) > 0:
    nextleg = corridor.pop(0)
    if nextleg[1] <= totalruntime: # run the whole way
      totaltime += nextleg[1]
      totalruntime -= nextleg[1]
    elif runtime > 0: # run part of the way on that corridor
      distrun = ((nextleg[0] + r) * totalruntime)
      totaldist = nextleg[4] - nextleg[3]
      togo = totaldist - distrun
      remtime = float(togo) / float(nextleg[0]+s)
      totaltime += remtime + totalruntime
      totalruntime = 0
    else: # have to walk the whole way
      totaltime += nextleg[2]
  out.write("Case #" + str(case+1) + ": " + str(totaltime) + "\n")
