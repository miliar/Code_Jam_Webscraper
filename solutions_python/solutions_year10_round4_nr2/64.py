import sys
import re
from Numeric import *
#from decimal import *

# ---------------------------------------------------------------------------------------------------------------

sys.setcheckinterval(10000)
PI = arccos(-1)
PI_2 = arccos(-1) / 2

#getcontext().prec = 200
#getcontext().rounding = ROUND_DOWN

# ---------------------------------------------------------------------------------------------------------------


def solve(caseNum):
  p = int(sys.stdin.readline().strip())
  m = map(int, sys.stdin.readline().strip().split(" "))
  needs = map(lambda x: p-x , m)
  prices = []
  go = []

  for r in range(0, p):
    prices.append(map(int, sys.stdin.readline().strip().split(" ")))
    go.append([False]  * len(prices[r]))
  res = 0

  for x in range(0, p):
    r = p - x - 1
    matches = len(m) /(2**(r+1))
    for match in range(0, matches):
      pm = len(m) / matches
      teamS = pm * match
      teamE = pm * (match+1)
      buy = False
      for t in range(teamS, teamE):
        if needs[t] > 0:
          needs[t] -= 1
          buy = True
      if buy: res += 1

  sys.stdout.write("Case #%d: %d" % (caseNum, res))

# ---------------------------------------------------------------------------------------------------------------

casesCount = int(re.findall(r'[\d]+', sys.stdin.readline())[0])
first = True
for case in range(1, casesCount + 1):
	if(first):
		first = False
	else:
		print ""
	solve(case)
