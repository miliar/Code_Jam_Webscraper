import sys, os

def algo(r, k, g, gps):
  start = 0
  mem = {}
  rmem = r
  money = 0
  # find possibilities
  while r>0:
    if mem.has_key(start) == False:
      s = 0
      istart = start
      while(s+gps[start]<=k):
        s += gps[start]
        start = (start+1) % g
        if(start==istart):
          break
      money += s
      mem[istart] = (start, s)
      r -= 1
    else:
      break
  if r>0:
      # determine loop length
      istart = start
      count = 1
      moneyinloop = mem[start][1]
      while(mem[start][0] != istart):
         start = mem[start][0]
         moneyinloop += mem[start][1]
         count += 1
      money += moneyinloop*int(r/count)
      r = r % count
      start = istart
      while r > 0:
        money += mem[start][1]
        start = mem[start][0]
        r -= 1
  return money

fd = open(sys.argv[1], "r")
num = int(fd.readline())
for i in range(num):
  inp = fd.readline()
  inp = inp.split(" ")
  r = int(inp[0])
  k = int(inp[1])
  g = int(inp[2])
  inp = fd.readline()
  inp = inp.split(" ")
  gps = []
  for gp in inp:
    gps += [int(gp)]
  print "Case #%d: %s" % (i+1, algo(r, k, g, gps))
  