input = open('C:\Documents and Settings\Administrator\My Documents\GCJ\Saving the Universe\A-large.in','r')
output = open('C:\Documents and Settings\Administrator\My Documents\GCJ\Saving the Universe\A-large.out','w')

engines = []
queries = []

def maxpos(start):
  positions = []
  for engine in engines:
    if start >= len(queries):
      return 1000
    if engine != queries[start]:
      try:
        positions.append(queries.index(engine,start))
      except:
        return 1000
  
  return max(positions)
  
  switches = []
  for eng in engines:
    if eng != engine:
      switches.append(minswitch(engine,pos + 1))
  return min(switches) + 1

for case in range(int(input.readline())):
  nengines = int(input.readline())
  engines = []
  for i in range(nengines):
    engines.append(input.readline().strip())
  
  nqueries = int(input.readline())
  queries = []
  for i in range(nqueries):
    queries.append(input.readline().strip())
  
  switches,pos = 0,0
  while maxpos(pos) < 1000:
    switches += 1
    pos = maxpos(pos)
  
  output.write("Case #%s: %s\n" % (case + 1, switches))

output.close()
input.close()