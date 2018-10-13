
CASES = int(raw_input())

for C in range(CASES):
  combs = {}
  rejs = {}
  inp = raw_input().split()

  n = int(inp.pop(0))
  for i in range(n):
    combs[inp[0][:-1]] = inp[0][-1]
    combs[inp[0][1] + inp[0][0]] = inp[0][-1]
    inp.pop(0)

  n = int(inp.pop(0))
  for i in range(n):
    rejs.setdefault(inp[0][0], []).append(inp[0][1])
    rejs.setdefault(inp[0][1], []).append(inp[0][0])
    inp.pop(0)

  invs = inp[-1]

  #print(combs)
  #print(rejs)
  #print(invs)

  EL = ''

  for c in invs:
    EL += c
    while any(EL.endswith(x) for x in combs):
      EL = EL[:-2] + combs[EL[-2:]]
      
    if any(x in EL for x in rejs.get(EL[-1], [])):
      EL = ''


  print 'Case #%d: [%s]' % (C+1, ', '.join(EL))


  

