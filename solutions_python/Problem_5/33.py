import sys

def parseInput(fname):
  f = open(fname, 'r')
  text = f.readlines()
  f.close()

  testCases = []
  cases = int(text[0])
  cnt = 1
  for i in range(cases):
    case = []
    numFlavors = int(text[cnt])
    cnt += 1
    numCustomers = int(text[cnt])
    cnt += 1
    customers = []
    for j in range(numCustomers):
      customer = []
      rawcust = text[cnt].split(" ")
      
      types = int(rawcust[0])
      cnt2 = 1
      for k in range(types):
        shake = int(rawcust[cnt2])
        cnt2 += 1
        like = int(rawcust[cnt2])
        cnt2 += 1
        customer.append((shake,like))
      
      customers.append((types,customer))
      cnt += 1
        
    testCases.append((numFlavors, numCustomers, customers))
  return testCases


def runCase(case):
  # generate all permutations of malted, unmalted
  t = exhaust(case, [], case[0])
  if t:
    t = [str(m) for m in t]
    return " ".join(t)
  return "IMPOSSIBLE"
  
def exhaust(case, state, n):
  if len(state)==n:
    return testState(state, case)
  t = exhaust(case, state + [0], n)
  if t:
    return t
  t = exhaust(case, state + [1], n)
  if t:
    return t
  return []

def testState(state, case):
  for types, customer in case[2]:
    found = False
    for shake, malted in customer:
      if state[shake-1] == malted:
        found = True
        break
    if not found:
      return False
  return state


def main(inputs=["test"]):
  for inputf in inputs:
    cases = parseInput(inputf+".in")
    res = []
    i = 1
    for case in cases:
      res.append((i,runCase(case)))
      i += 1

    
    output = ["\n".join("Case #%s: %s" % (num, ans) for num,ans in res)]
    outf = open(inputf+".out",'w')
    outf.write("\n".join("Case #%s: %s" % (num, ans) for num,ans in res))
    outf.close()

if __name__=="__main__":
  if sys.argv[1:]:
    main(sys.argv[1:])
  else:
    main()
