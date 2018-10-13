from collections import defaultdict

def stalls(nstalls, npeople):
  if nstalls==1:# or npeople>(nstalls+2)/2:
    return 0, 0
  exp = 1
  while 2**exp < npeople+1:
    exp += 1
  slots = 2**(exp-1)
  stallcounter = defaultdict(int)
  basenum = -1 + (nstalls+1) / (slots*2)
  leftover = (nstalls+1) % (slots*2)
  stallcounter[(basenum, basenum)] = slots
  if leftover > 0:
    to_add = min(leftover, slots)
    stallcounter[(basenum, basenum)] -= to_add
    stallcounter[(basenum, basenum+1)] += to_add
  if stallcounter[(basenum, basenum)] ==0:
    del stallcounter[(basenum, basenum)]
  if leftover > slots:
    to_add = leftover - slots
    stallcounter[(basenum, basenum+1)] -= to_add
    stallcounter[(basenum+1, basenum+1)] += to_add
  stallsorted = sorted(stallcounter.items(), key=lambda x : (min(x[0]), max(x[0])), reverse=True)
  #print stallsorted
  counter = slots-1
  loc = 0
  #print counter
  while counter < npeople and loc<len(stallsorted):
    counter += stallsorted[loc][1]
    loc += 1
  #print "after"
  #print counter, loc
  if loc==len(stallsorted) and counter < npeople:
    return 0, 0
  return max(stallsorted[loc-1][0]), min(stallsorted[loc-1][0])
 
ncases = int(raw_input().strip())
for i in xrange(1, ncases+1):
  args = map(int, raw_input().strip().split(" "))
  res = stalls(args[0], args[1])
  print "Case #%d: %d %d" % (i, res[0], res[1])
