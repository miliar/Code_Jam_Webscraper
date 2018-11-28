
def checkElems(arr, elem):
  
  for i in xrange(4):
    if arr[i].count(elem) == 4 or (arr[i].count(elem)==3 and "T" in arr[i]):
      return True
  temp = []
  for i in xrange(4):
    temp.append([])
    temp[i].append(arr[0][i])
    temp[i].append(arr[1][i])
    temp[i].append(arr[2][i])
    temp[i].append(arr[3][i])
    
  for i in xrange(4):
    if temp[i].count(elem) == 4 or (temp[i].count(elem)==3 and "T" in temp[i]):
      return True
  
  temp = []
  temp.append([])
  for i in xrange(4):
    temp[0].append(arr[i][i])
  temp.append([])
  x = 3
  y = 0
  for i in xrange(4):
    temp[1].append(arr[y][x])
    y +=1
    x -=1
    
  for i in xrange(2):
    if temp[i].count(elem) == 4 or (temp[i].count(elem)==3 and "T" in temp[i]):
      return True    
  
  return False

def checkDraw(arr):
  for i in xrange(4):
    if '.' in arr[i]:
      return False
  return True

f = open("A-small-attempt0.in","r")
out = open("output.txt","w")

count = int(f.readline())

counter = 0
for i in xrange(count):
  counter +=1
  arr = []
  for j in xrange(4):
    arr.append([])
    x = f.readline().strip()
    if not x:
      x = list(f.readline().strip())
    else:
      x = list(x)
    for k in x:
      arr[j].append(k)

  if(checkElems(arr, 'X')):
    print "Case #" + str(counter) + ": X won"
    continue
  elif(checkElems(arr,'O')):
    print "Case #" + str(counter) + ": O won"
    continue
  elif(checkDraw(arr)):
    print "Case #" + str(counter) + ": Draw"
  else:
    print "Case #" + str(counter) + ": Game has not completed"
  
out.close()
f.close()