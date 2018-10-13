ncases = int( raw_input() )

for n in xrange(ncases):
  C, F, X = [float(v) for v in raw_input().strip().split(" ")]
  bal = 0; rate = 2; ans = 0; elapsed = 0;
  while bal != X:
    buyTime = (C-bal) / rate
    endTime = (X-bal) / rate
    if endTime < buyTime:
      ans = elapsed + endTime
      break
    elif buyTime + X / (rate + F) < (X-bal) / rate:
      elapsed += buyTime
      bal = 0
      rate += F
    else:
      ans = elapsed + endTime
      break
  
  print "Case #%d: %.9f" %(n+1, ans)
