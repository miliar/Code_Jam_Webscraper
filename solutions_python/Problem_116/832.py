filein = open('A-large.in', 'r')
filein.readline()
fileline = ''
fileout = open('A-large-output.in', 'w')

newListLine = []
for line in filein:
  fileline = fileline+line
  listLine = fileline.split('\n\n')

listLine.remove(listLine[-1])

for each in listLine:
  tmp = each.split('\n')
  newListLine.append(tmp)

i = 1
for each in newListLine:
  listResultLine = []
  for word in each:
    listResultWord = ''
    listResultWord = listResultWord+word
    listResultLine.append(listResultWord)
  #print listResultLine
  strResult = ''
  s0 = listResultLine[0][0]+listResultLine[0][1]+listResultLine[0][2]+listResultLine[0][3]
  s1 = listResultLine[1][0]+listResultLine[1][1]+listResultLine[1][2]+listResultLine[1][3]
  s2 = listResultLine[2][0]+listResultLine[2][1]+listResultLine[2][2]+listResultLine[2][3]
  s3 = listResultLine[3][0]+listResultLine[3][1]+listResultLine[3][2]+listResultLine[3][3]
  s4 = listResultLine[0][0]+listResultLine[1][0]+listResultLine[2][0]+listResultLine[3][0]
  s5 = listResultLine[0][1]+listResultLine[1][1]+listResultLine[2][1]+listResultLine[3][1]
  s6 = listResultLine[0][2]+listResultLine[1][2]+listResultLine[2][2]+listResultLine[3][2]
  s7 = listResultLine[0][3]+listResultLine[1][3]+listResultLine[2][3]+listResultLine[3][3]
  s8 = listResultLine[0][0]+listResultLine[1][1]+listResultLine[2][2]+listResultLine[3][3]
  s9 = listResultLine[0][3]+listResultLine[1][2]+listResultLine[2][1]+listResultLine[3][0]
  strResult = s0+','+s1+','+s2+','+s3+','+s4+','+s5+','+s6+','+s7+','+s8+','+s9
  qiPan = s0+s1+s2+s3
  #print strResult
  #print qiPan
  #print i
  if('XXXX' in strResult or 'XXXT' in strResult or 'XXTX' in strResult or 'XTXX' in strResult or 'TXXX' in strResult):
    result = 'X won'
  elif('OOOO' in strResult or 'OOOT' in strResult or 'OOTO' in strResult or 'OTOO' in strResult or 'TOOO' in strResult):
    result = 'O won'
  elif(not ('.') in qiPan):
    result = 'Draw'
  else:
    result = 'Game has not completed'
  result = 'Case #'+str(i)+': '+result+'\n'
  fileout.write(result)
  i = i+1

filein.close()
fileout.close()

