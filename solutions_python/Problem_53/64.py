import sys, os
class snapper:
  def __init__(self):
    self.power = 0
    self.state = 0
def algo2(n, k):
  count = 2 ** n
  k = k % count
  if k == count-1:
    return "ON"
  else:
    return "OFF"
def algo(n, k):
  snappers = []
  for i in range(n):
    snappers += [snapper()]
  snappers[0].power = 1
  for i in range(k):
    for j in range(n):
      if snappers[j].power == 1:
        snappers[j].state = 1 - snappers[j].state
    for j in range(1,n):
      snappers[j].power = 0
    j=1;
    while(j<n and snappers[j-1].power == 1 and snappers[j-1].state == 1):
      snappers[j].power = 1
      j += 1
  if snappers[n-1].power == 1 and snappers[n-1].state == 1:
    return "ON"
  else:
    return "OFF"

fd = open(sys.argv[1], "r")
num = int(fd.readline())
for i in range(num):
  inp = fd.readline()
  inp = inp.split(" ")
  n = int(inp[0])
  k = int(inp[1])
  print "Case #%d: %s" % (i+1, algo2(n,k))
  