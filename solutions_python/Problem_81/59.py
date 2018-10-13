data = [l.strip() for l in open("infile", "r").readlines()]
out = open("outfile", "w")

numcases = int(data.pop(0))
for case in range(numcases):
  numteams = int(data.pop(0))
  teamdata = []
  for team in range(numteams):
    teamdata.append(list(data.pop(0)))
  # make new matrix
  moredata = [['?' for i in range(numteams)] for j in range(numteams)]
  for team in range(numteams):
    record = [0, 0] # wins, games played
    for i in teamdata[team]: # yes, I know, there is no "I" in team
      if i == '1':
        record[0] += 1
        record[1] += 1
      elif i == '0':
        record[1] += 1
    moredata[team][team] = record # these now have the WP values
  # now calculate OWP
  for team1 in range(numteams):  # OWP for this team...
    for team2 in range(team1+1, numteams): # from the perspective of this team
      if teamdata[team1][team2] == '.':
        moredata[team1][team2] = '.'
        moredata[team2][team1] = '.'
      else:
        newdata1 = [moredata[team1][team1][0], moredata[team1][team1][1]]
        newdata2 = [moredata[team2][team2][0], moredata[team2][team2][1]]      
        if teamdata[team1][team2] == '1':
          newdata1[0] -= 1
          newdata1[1] -= 1
          newdata2[1] -= 1
        else:
          newdata1[1] -= 1
          newdata2[0] -= 1
          newdata2[1] -= 1
        moredata[team1][team2] = newdata1
        moredata[team2][team1] = newdata2
  out.write("Case #" + str(case+1) + ":\n")
  # convert
  for i in range(numteams):
    for j in range(numteams):
      if moredata[i][j] != '.':
        moredata[i][j] = float(moredata[i][j][0]) / float(moredata[i][j][1])   
  # find each team's OWP
  for i in range(numteams):
    owptotal = 0.0
    numopps = 0
    for j in range(numteams):
      if moredata[j][i] != '.' and i != j:
        numopps += 1
        owptotal += moredata[j][i]
    owp = owptotal / float(numopps)
    moredata[i].append(owp)
  for i in range(numteams):
    oowptotal = 0
    numopps = 0
    for j in range(numteams):
      if i != j:
        if moredata[i][j] != '.':
          numopps += 1
          oowptotal += moredata[j][numteams]
    oowp = oowptotal / float(numopps)
    rpi = .25 * moredata[i][i] + .50 * moredata[i][numteams] + .25 * oowp
    out.write(str(rpi) + "\n")

