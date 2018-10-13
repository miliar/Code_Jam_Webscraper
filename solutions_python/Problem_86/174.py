ntests = int(raw_input())
for test in xrange(ntests):
  info = map(long,raw_input().split())
  players = map(long,raw_input().split())
#  print
#  print
#  print info
#  print players
  h = info[2]
  l = info[1]
  i=0
  e=0
  results = {}
  for i in xrange(l,h+1):
    v = i
    valid = True
    for e in xrange(len(players)):
      if(v%players[e]!=0 and players[e]%v!=0):
        valid = False
        break
        
    if(valid):
      break
      
      
  if(valid):
    print "Case #%d: %d" % (test+1,v)
  else:
    print "Case #%d: NO" % (test+1)