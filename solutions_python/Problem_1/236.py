import sys

inputcases = int(sys.stdin.readline())
for case in range(inputcases):
  inputengines = int(sys.stdin.readline())
  engines = {}
  for i in range(inputengines):
    engines[sys.stdin.readline().strip()] = i
  inputqueries = int(sys.stdin.readline())
  queries = []
  for i in range(inputqueries):
    queries.append(sys.stdin.readline().strip())

  #print engines.keys()
  #print queries

  switches = 0

  counts = [0]*len(engines)
  for i in range(len(queries)):

    nextquery = engines[queries[i]]
    if len([a for a in counts if a == 0]) == 1 and counts[nextquery] == 0:
      #print queries[i] # switch from. clear the counts
      switches += 1
      counts = [0]*len(engines)
    counts[nextquery] += 1

  print 'Case #%d: %d' % (case+1, switches)

  #print engines
  #print counts
