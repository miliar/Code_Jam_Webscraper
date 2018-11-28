input = open('B-large.in')

test_num = int(input.readline().split()[0])

for i in range(test_num):
  C, F, X = [float(x) for x in input.readline().split()]
  th = (F*X-2*C)/(F*C)
  A = int(th)
  if A < 0:
  	A = 0
  ans = 0
  for n in range(A):
  	ans += C/(2+n*F)
  ans += X/(2+A*F)
  print 'Case #%d:' % (i+1), round(ans, 7)