T = input()
for i in range(1,T+1):
  nums = raw_input()
  C,F,X = map(float,nums.split())
  speed = 2.0
  time = 0.0
  est = X/speed
  est2 = C/speed + X/(speed+F)
  while(est>est2):
    time += C/speed
    speed += F
    est = X/speed
    est2 = C/speed + X/(speed+F)
  result = time + X/speed
  print "Case #%d: %.7f" % (i,result)
