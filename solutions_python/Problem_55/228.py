import numpy
import fractions

outputF = 'Coaster.txt'
inputF = '/Users/sholte/Downloads/C-small-attempt0.in'
#inputF = '../test.in'

output = open(outputF,'w')

def getint(f):
  return int(f.readline())

def getints(f):
  return [int(x) for x in f.readline().split()]

def parse(file):
  f = open(file)
  n =  getint(f)
  for i in range(n):
    ints = getints(f)
    ints2 = getints(f)
    r = onecase(i+1,ints,ints2)
    print >>output,"Case #%d: %d"%(i+1,r)
    
  return

def onecase(case,ints,ints2):
  R,k,N = ints
  groups = numpy.array(ints2)
  assert(len(groups==N))
  wrap = numpy.concatenate((groups,groups))
  cGroups = wrap.cumsum()
  total = cGroups[N-1]
  if total<k:
     return total*R;
  oldCount = numpy.concatenate(([0],cGroups[:N-1]))
  kGroups = oldCount+k
  sGroups = numpy.searchsorted(cGroups,kGroups,'right')
  next = sGroups%N
  newCount = cGroups[sGroups-1]
  profit = newCount-oldCount
  
  currI = 0
  totalProfit=0
  totalSteps=0
  step = [-1 for i in range(N)];
  netProfit = [0 for i in range(N)]
  while(R>totalSteps and step[currI]==-1):
    step[currI]=totalSteps
    totalSteps+=1
    netProfit[currI]=totalProfit
    totalProfit+=profit[currI]
    currI = next[currI]
  
  print R,k,groups
  print 'Cycle at',totalSteps,R,currI,step[currI],totalProfit
  if(step[currI]!=-1):
    cycleSteps=totalSteps-step[currI]
    cycles=int((R-totalSteps)/cycleSteps)
    totalSteps+=cycleSteps*cycles
    cycleProfit=totalProfit-netProfit[currI]
    totalProfit+=cycles*cycleProfit
    print 'Added',cycles,cycleSteps,cycleProfit
    print 'Reached',totalSteps,totalProfit
  
  while(R>totalSteps):
    totalSteps+=1
    totalProfit+=profit[currI]
    currI=next[currI]
  
  
  return totalProfit

print "Reading:"+inputF
print "Writing:"+outputF
parse(inputF)