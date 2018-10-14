cases = int(raw_input())
for z in xrange(1, (cases+1)):
  c,f,x = map(float, raw_input().split())
  cookies = 0
  cps = 2.0
  time = 0.0
  target = x
  wineta = target/cps
  farmeta = c/cps
  while target > 0:
    if wineta <= (farmeta + (target/(cps+f))) :
      target = 0
      time += wineta
    else:
      time += farmeta
      cps += f
      wineta = target/cps
      farmeta = c/cps
  print "Case #" + str(z) + ": " + str("%.7f" % round(time,7))
