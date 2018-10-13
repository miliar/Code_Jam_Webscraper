tc = int(input())
tot = tc
while tc:
  tc -= 1
  inp = raw_input().split()
  r = int(inp[0])
  t = int(inp[1])
  #Processing of data starts here
  area = 0
  ind = 0
  #For first ring
  cons = 1 + 2*r
  area += cons + 4*ind
  while area<=t:
    ind += 1
    area += cons + 4*ind
  print "Case #"+str(tot-tc)+": "+str(ind)
