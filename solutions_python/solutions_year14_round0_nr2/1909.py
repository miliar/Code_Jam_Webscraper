def decide(c,f,x):
  tFinnish = x/r
  tBuild = (c/r)+(x/(r+f))
  
  if tBuild < tFinnish:
    return 'build'
  else:
    return 'finnish'

fileVar = file('B-large.in','r')

numTrials = int(fileVar.readline().rstrip())

for t in range(numTrials):
  time = 0
  data = fileVar.readline().rstrip().split()
  c = float(data[0])
  f = float(data[1])
  x = float(data[2])
  r = 2

  done = False

  while(not done):
    ans = decide(c,f,x)
    if ans == 'finnish':
      time += x/r
      done = True
    if ans == 'build':
      time += c/r
      r += f
  print "Case #"+str(t+1)+": "+str(time)
