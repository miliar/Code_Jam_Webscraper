
def botTrust(line):
  l = line.split(" ")
  n = int(l[0])
  idx = 1
  rst = 0
  lastOBotPos = '1'
  lastBBotPos = '1'
  OBotTime = 0
  BBotTime = 0

  while(idx <= n*2-1):
    if(idx == 1):
      lastBot = l[idx]
      lastPos = l[idx+1]
      if(l[idx] == 'O'):
        lastOBotPos = l[idx+1]
        OBotTime = int(lastPos)
      else:
        lastBBotPos = l[idx+1]
        BBotTime = int(lastPos)
      idx = idx + 2
      continue
   
    if(l[idx] == lastBot):
      lastPos = l[idx+1]
      lastBot = l[idx]
      if(l[idx]=='O'):
        #rst = rst + (int(l[idx+1])) - int(lastOBotPos)) + 1
        OBotTime = OBotTime + abs((int(l[idx+1])) - int(lastOBotPos)) + 1
        lastOBotPos = l[idx+1]
        #OBotTime = OBotTime + abs((int(l[idx+1])) - int(lastOBotPos)) + 1
      else:
        #rst = rst + (int(l[idx+1])) - int(lastBBotPos)) + 1
        BBotTime = BBotTime + abs((int(l[idx+1])) - int(lastBBotPos)) + 1
        lastBBotPos = l[idx+1]
        #BBotTime = BBotTime + abs((int(l[idx+1])) - int(lastBBotPos)) + 1
      idx = idx + 2
      continue

    if(l[idx] != lastBot):
      lastBot = l[idx]
      lastPos = l[idx+1]
      if(l[idx]=='O'):
        OBotTime = OBotTime + abs((int(l[idx+1])) - int(lastOBotPos)) + 1
        lastOBotPos = l[idx+1]
        if(BBotTime >= OBotTime):
          OBotTime = BBotTime + 1
        else: 
          OBotTime = OBotTime
          #print str(idx) + " " + str(OBotTime) + str(BBotTime) + "\n"
      else:
        BBotTime = BBotTime + abs((int(l[idx+1])) - int(lastBBotPos)) + 1
        lastBBotPos = l[idx+1]
        if(OBotTime >= BBotTime):
          BBotTime = OBotTime + 1
          #print str(idx) + " " + str(OBotTime) + " " + str(BBotTime) + "\n"
        else:
          BBotTime = BBotTime
          #print str(idx) + " " + str(BBotTime)
      idx = idx + 2
      continue
  
  if(OBotTime>BBotTime):
    return OBotTime
  else:
    return BBotTime

