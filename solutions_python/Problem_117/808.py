filein = open('B-large.in', 'r')
filein.readline()
fileout = open('b-large-output.in', 'w')

total = []
lenTotal = 0
for line in filein:
  lenTotal = lenTotal+1
  line = line[:-1]
  line = line.split(' ')
  intLine = []
  for each in line:
    each =  int(each)
    intLine.append(each)
  total.append(intLine)

def possible(matrix):
  listMaxHang = []
  listMaxLie = []
  result = []
  for hang in range(0, len(matrix)):
    maxHang = max(matrix[hang])
    listMaxHang.append(maxHang)
  for lie in range(0, len(matrix[0])):
    listLie = []
    for hang in range(len(matrix)):
      #listLie = []
      listLie.append(matrix[hang][lie])
    maxLie = max(listLie)
    listMaxLie.append(maxLie)
  for hang in range(0, len(matrix)):
    for lie in range(0, len(matrix[0])):
      if(matrix[hang][lie] != min(listMaxHang[hang], listMaxLie[lie])):
        result.append('NO')
      else:
        result.append('YES')
  if('NO' in result):
    return 0
  else:
    return 1

temp = lenTotal
i = 0
j = 1
while(temp > 0):
  num = total[i][0]
  matrix = []
  tmp = int(num)
  while(tmp > 0):
    matrix.append(total[i+1])
    i = i+1
    tmp = tmp-1
  i = i+1
  temp = temp-int(num)-1
  final = possible(matrix)
  news = 'Case #'+str(j)+': '
  if final:
    news = news+'YES\n'
  else:
    news = news+'NO\n'
  j = j+1
  fileout.write(news)

fileout.close()
filein.close()




filein.close()
