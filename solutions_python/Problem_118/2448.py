def printResult(i, out):
  print "Case #"+str(i)+": "+str(out)

def getCases():
  f=open("C-small-attempt0.in")
  T = int(f.readline())
  cases  = []
  for t in xrange(T):
    cases.append(map(int,f.readline().split(" ")))
  return cases

def process(T,K):
  count = 0
  for i in range(31):
    if (i - int(str(i)[::-1]) ==0):
      sqr = i*i
      if sqr<T:
        continue
      elif sqr>K:
        break

      if(sqr - int(str(sqr)[::-1]) ==0):
        count = count + 1
  return count

for i,rng in enumerate(getCases()):
  printResult(i+1, process(rng[0],rng[1]))

