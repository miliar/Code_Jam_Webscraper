def help(r, c):
  if r > 1 and c > 1: return 1
  else: return 0

def solve(x, r, c):
  if x > r*c: ans = "RICHARD"
  else:
    if x > 2 and help(r, c) == 0: ans = "RICHARD"
    else:
      if (r*c)%x == 0: 
	if x == 4 and (r == 2 or c == 2): ans = "RICHARD"
	else: ans = "GABRIEL"
      else: ans = "RICHARD"
  return ans

cases = input()
for caseN in xrange(1, cases+1):
  audi = map(int, raw_input().split())
  print("Case #%i: %s" % (caseN, solve(audi[0], audi[1], audi[2])))

