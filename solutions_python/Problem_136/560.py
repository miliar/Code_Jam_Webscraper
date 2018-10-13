cps = 2.0

def main():
   c, f, x = map(float, raw_input().split())
   farmsused = 0
   timetogetfarms = 0
   timetowin = x/cps
   while True:
      timetogetfarms += c/(farmsused*f+cps)
      farmsused += 1
      cand = timetogetfarms + x/(farmsused*f+cps)
      if cand < timetowin:
         timetowin = cand
      else:
         break
   return timetowin

T = input()
for i in xrange(T):
   print "Case #%s: %s" % (i+1, main())
      

