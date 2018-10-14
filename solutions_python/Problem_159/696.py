def solve(p, n):
  tmp, r1, r2 = 0, 0, 0
  for i in range(1, n):
  	diff = p[i-1] - p[i]
  	if diff >=0: r1 += diff
  	tmp = max(tmp, diff)
  for i in range(n-1):
  	r2 += (p[i] if p[i] <= tmp else tmp)
  return str(r1) + ' ' + str(r2)

cases = input()
for caseN in xrange(1, cases+1):
  n = input()
  mush = map(int, raw_input().split())
  print("Case #%i: %s" % (caseN, solve(mush, n)))

