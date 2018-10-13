import sys

def parseInput(fname):
  f = open(fname, 'r')
  text = f.readlines()
  f.close()

  testCases = []
  cases = int(text[0])
  cnt = 1
  for i in range(cases):
    engines = {}
    queries = []
    numEngines = int(text[cnt])
    cnt += 1
    for j in range(numEngines):
      engines[text[cnt].strip()] = j
      cnt += 1

    numQueries = int(text[cnt])
    cnt += 1
    for j in range(numQueries):
      queries.append(text[cnt].strip())
      cnt += 1

    testCases.append((engines, queries))
  return testCases


def runCase(case):
  engine_to_index = case[0]
  queries = case[1]

  INFINITY = 100000

  lastState = [0]*len(engine_to_index)
  curState = [0]*len(engine_to_index)

  for query in queries:
    for i in xrange(len(engine_to_index)):
      if i == engine_to_index[query]:
        curState[i] = INFINITY
      else:
        # print i,lastState[i], min(lastState[j]+1 for j in xrange(len(lastState)) if j != i)
        curState[i] = min(lastState[i],      # use same engine as last
                          min(lastState[j]+1 # cost of switching
                              for j in xrange(len(lastState))
                              if j != i))
    #print curState
    lastState = list(curState)
  return min(curState)

def main(inputs=["test","test2"]):
  for inputf in inputs:
    cases = parseInput(inputf+".in")
    res = []
    i = 1
    for case in cases:
      res.append((i,runCase(case)))
      i += 1
      
    output = ["\n".join("Case #%s: %s" % (num, ans) for num,ans in res)]
    print output
    outf = open(inputf+".out",'w')
    outf.write("\n".join("Case #%s: %s" % (num, ans) for num,ans in res))
    outf.close()

def genTestCase(numengines, numqueries):
  import random
  print "generating with %s engines and %s queries" % (numengines, numqueries)
  engines = range(numengines)
  engines = [str(en) for en in engines]
  ret = [str(numengines)]
  ret.extend(engines)

  ret.append(str(numqueries))
  for i in range(numqueries):
    ret.append(str(random.randint(0,numengines-1)))
  return ret

def genTestFile():
  f = open('test4.in','w')
  f.write('10\n')
  for i in range(10):
    f.write('\n'.join(genTestCase(10+10*i,1000)))
    f.write('\n')
  f.close()

if __name__=="__main__":
  if sys.argv[1:]:
    main(sys.argv[1:])
  else:
    main()
