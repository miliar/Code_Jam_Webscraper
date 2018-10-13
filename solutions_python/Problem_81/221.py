file = open("input.in","r")

lines = file.readlines()

T = int(lines[0].rstrip())

pointer = 1
for w in range(T):
  N = int(lines[pointer].rstrip())
  pointer += 1

  M = {}
  for i in range(N):
    line = lines[pointer].rstrip()
    for j in range(len(line)):
        M[ (i,j) ] = line[j]
    pointer += 1

  WP = {}
  for i in range(0,N):
    total = 0
    won = 0 
    for j in range(0,N):
      if M[ (i,j) ] == "1":
        won += 1
        total += 1
      if M[ (i,j) ] == "0":
        total += 1
    if total == 0:
      WP[i] = 0
    else:
      WP[i] = float(won)/total

  OWP = {}
  for i in range(0,N):
    WPO = {}
    for x in range(0,N):
      if (M[ (i,x) ] == "1") or (M[ (i,x) ] == "0"):
        total = 0
        won = 0
        for y in range(0,N):
          if x != i and y != i:
            if M[ (x,y) ] == "1":
              won += 1
              total += 1
            if M[ (x,y) ] == "0":
              total += 1
        if total == 0:
          WPO[x] = 0
        else:
          WPO[x] = float(won)/total
    total = 0
    for x in WPO.keys():
      total += WPO[x]
    OWP[i]=total/len(WPO.keys())

  OOWP = {}
  for i in range(0,N):
    total = 0
    nr = 0
    for x in range(0,N):
      if (M[ (i,x) ] == "1") or (M[ (i,x) ] == "0"):
        total += OWP[x]
        nr += 1
    OOWP[i] = total/nr

  RPI = {}
  print "Case #"+str(w+1)+":"
  for i in range(0,N):
    RPI[i] = 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i]
    print RPI[i]
