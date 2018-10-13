N = input()
for k in range(N):
  T = input()
  table = []
  teams = {}
  for i in range(T):
    teams[i] = {}

  for i in range(T):
    s = raw_input()
    for j in range(T):
      if s[j] != '.':
        teams[i][j] = int(s[j])
        teams[j][i] = 0 if int(s[j]) else 1

  wps = {}
  for i in teams:
    wps[i] = sum(teams[i].values())/float(len(teams[i]))

  
  owps = {}
  for i in teams:
    s = 0
    for o in teams[i]:

      som = sum(teams[o].values()) - teams[o][i]
      played = len(teams[o]) - 1.
      s += som/played
    owps[i] = s / len(teams[i])

  oowps = {}
  for i in teams:
    oowps[i] = sum(owps[c] for c in teams[i])/ float(len(teams[i]))
  
  rpis = {}
  for i in teams:
    rpis[i] = 0.25*wps[i] + 0.5*owps[i] + 0.25 * oowps[i]

  print "Case #%d:" % (k+1)
  for i in range(T):
    print rpis[i]


