def minTime(fCst, fRt, trgt):
  trgtRchd = False
  time = 0.0
  numFrm = 0
  Rt = 2.0
  while not trgtRchd:
    curTime = trgt / Rt
    xtrFrmTime = fCst / Rt    # Time to get a new farm
    Rt += fRt
    newTime = trgt / Rt + xtrFrmTime  #time to reach target along with new farm
    if newTime >= curTime :
      time += curTime
      trgtRchd = True
    else :
      numFrm += 1
      time += xtrFrmTime
  return time


fileIn = open("B-large.in", 'r')
fileOut = open('file.out', 'w')
tCases = int(fileIn.readline())
curCase = 0
while tCases > curCase :
  op = 'Case #' + str(curCase + 1) + ': '
  cookie = [float(i) for i in fileIn.readline().split(' ')]
  time = minTime(cookie[0], cookie[1], cookie[2])
  op += str(time) + '\n'
  fileOut.write(op)
  curCase += 1
fileIn.close()
fileOut.close()
