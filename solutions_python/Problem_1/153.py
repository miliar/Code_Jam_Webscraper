out = open('A-out-large.txt', 'w')

def read(filename):
  f = open(filename)
  cases = int(f.readline())

  for i in range(cases):
    engines = []
    num = int(f.readline())
    for j in range(num):
      engines.append(f.readline()[:-1])
    
    queries = []
    num = int(f.readline())
    for j in range(num):
      queries.append(f.readline()[:-1])

    ans = doIt(engines, queries)
    out.write("Case #%d: %d\n" % (i+1, ans))

  f.close()

def doIt(engines, queries):
  
  ans = 0
  while len(queries)>0:
    dist = []
    for i in engines:
      try: dist.append(queries.index(i))
      except ValueError: dist.append(100000000)
    
    m = max(dist)
    
    if m == 100000000:
      return ans

    queries = queries[m:]

    ans += 1

  return 0

read('A-large.in')

out.close()