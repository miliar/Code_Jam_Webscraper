filein = open('C-small-attempt0.in', 'r')
filein.readline()
fileout = open('C-small-output.in', 'w')

fileline = []
for line in filein:
  fileline.append(line)

def fairAndSquare(a, b):
  count = 0
  for i in range(a, b+1):
    strI = str(i)
    newStrI = strI[::-1]
    if(strI == newStrI):
      sq = i**0.5
      tmp = int(sq)
      if(tmp**2 == i):
        sq = int(sq)
        strSq = str(sq)
        newStrSq = strSq[::-1]
        if(strSq == newStrSq):
          count = count+1
  return count

i = 1
for line in fileline:
  news = 'Case #'+str(i)+': '
  listLine = line.split(' ')
  a = int(listLine[0])
  b = int(listLine[1])
  count = fairAndSquare(a, b)
  news = news+str(count)+'\n'
  i = i+1
  fileout.write(news)

fileout.close()
filein.close()
