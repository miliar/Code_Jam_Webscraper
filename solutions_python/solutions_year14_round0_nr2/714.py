T = raw_input()
for t in range(int(T)):
  need = 0.
  C, F, X = map(float, raw_input().split())
  now = 2.
  while X / now > C/now + X/(now+F):
    need += C/now
    now += F
  
  print 'Case #%d:' % (t+1), need+X/now