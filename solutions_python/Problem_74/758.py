T = -1
f = open ('a.in', 'r')
for line in f:
  T += 1
  if T == 0: continue
  instr = line.split()
  instr = zip([int(x=='B') for x in instr[1::2]], 
              [int(x) for x in instr[2::2]])
  pos, time = [1, 1], [0, 0]
  for r, p in instr:
    time[r] += abs (pos[r] - p)
    pos[r] = p
    if time[1-r] >= time[r]:
      time[r] = time[1-r]
    time[r] += 1
    #print "v case", time[r], "robot", r
  print "Case #%d: %d" % (T, max (time[0], time[1]))

