N = input()
for k in range(N):
  s = raw_input().split()
  C = int(s.pop(0))
  combs = {}
  while C > 0:
    C-=1
    a,b,c = s.pop(0)
    combs[a+b] = c
    combs[b+a] = c
  D = int(s.pop(0))
  opposes = {}
  while D > 0:
    D-=1
    a,b = s.pop(0)
    opposes[a] = b
    opposes[b] = a
  invocation = s[-1]
  
  #print combs
  #print opposes
  result = ['']
  for c in invocation:
    # Combine
    last = result[-1]+c
    if last in combs:
      result[-1] = combs[last]
      continue
    
    # Oppose
    if c in opposes and opposes[c] in result:
      result = ['']
      continue
    
    # Add
    result.append(c)

  result.pop(0)
  print "Case #%d: [%s]" % (k+1, ', '.join(result))
