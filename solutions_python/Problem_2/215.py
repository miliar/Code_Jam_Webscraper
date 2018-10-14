import sys
from collections import defaultdict

def printTime(minutes):
  print "%2s:%2s"%(minutes/60,minutes%60)
  
def parseInput(fname):
  f = open(fname, 'r')
  text = f.readlines()
  f.close()

  testCases = []
  cases = int(text[0])
  cnt = 1
  for i in range(cases):
    timeout = int(text[cnt])
    cnt += 1
    
    na,nb = text[cnt].split(' ')
    na = int(na)
    nb = int(nb)
    cnt += 1
    
    atrips = defaultdict(list)
    btrips = defaultdict(list)

    for j in range(na):
      time1, time2 = text[cnt].strip().split(' ')
      time1 = time1.split(':')
      time2 = time2.split(':')
      atrips[int(time1[0])*60+int(time1[1])].append(int(time2[0])*60+int(time2[1])+timeout)
      cnt += 1

    for j in range(nb):
      time1, time2 = text[cnt].strip().split(' ')
      time1 = time1.split(':')
      time2 = time2.split(':')
      btrips[int(time1[0])*60+int(time1[1])].append(int(time2[0])*60+int(time2[1])+timeout)
      cnt += 1

    testCases.append((atrips, btrips))
  return testCases

def runCase(case):
  atrips = case[0]
  btrips = case[1]

  aneed = 0
  bneed = 0
  
  acount = 0
  bcount = 0

  # aqueue has arrival times of trains en route to a
  aqueue = defaultdict(lambda: 0)
  bqueue = defaultdict(lambda: 0)

  # cycle through day
  for i in range(1440):
    # add trains arriving at these times
    acount += aqueue[i]
    bcount += bqueue[i]

    #print "day %s: a: %s b: %s arrive_a: %s arrive_b: %s atrips: %s btrips: %s" % (i, acount,bcount,aqueue[i],bqueue[i], atrips[i], btrips[i])

    # handle leaving trains
    aleaving = atrips[i]
    if aleaving:
      # trains leaving
      acount = acount - len(aleaving)
      if acount < 0:
        aneed += abs(acount)
        acount = 0

      for train in aleaving:
        bqueue[train] += 1

    # handle leaving trains
    bleaving = btrips[i]
    if bleaving:
      # trains leaving
      bcount = bcount - len(bleaving)
      if bcount < 0:
        bneed += abs(bcount)
        bcount = 0
        
      for train in bleaving:
        aqueue[train] += 1

  return "%s %s" % (aneed,bneed)

def main(inputs=["test"]):
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


if __name__=="__main__":
  if sys.argv[1:]:
    main(sys.argv[1:])
  else:
    main()
