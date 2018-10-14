T = int(raw_input())

for i in xrange(T):
  size = int(raw_input())
  naomi = map(float, raw_input().split(" "))
  ken = map(float, raw_input().split(" "))

  naomi.sort()
  ken.sort()

  ki = 0

  wins = 0 
  for n in naomi:
    while ki < size and ken[ki] < n:
      wins += 1
      ki += 1
    ki += 1

  d_wins = 0
  ki = 0

  for n in naomi:
    if ken[ki] < n:
      d_wins += 1
      ki += 1

  print "Case #" + str(i+1) +":", d_wins, wins

