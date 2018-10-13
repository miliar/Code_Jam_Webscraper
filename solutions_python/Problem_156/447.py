def solve(p, n):
  glut = max(p)
  timer = glut
  for i in range(1, glut):
	tmp, maxval = 0, 0
	for j in p:
	  if j > i:
	  	tmp += (j/i) + (0 if j%i == 0 else 1) - 1
	  	maxval = max(maxval, i)
	  else: maxval = max(maxval, j)
	tmp += maxval
	if tmp < timer: timer = tmp
  return timer

cases = input()
for caseN in xrange(1, cases+1):
  n = input()
  audi = map(int, raw_input().split())
  print("Case #%i: %i" % (caseN, solve(audi, n)))

