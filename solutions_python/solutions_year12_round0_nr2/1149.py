#!/usr/bin/python4
import string
fname = 'small'
objfile = open('%s.in' % fname, 'r')
result = []
output = ''
num = 0
counter = 0
splitStr = []
noOfGooglers = 0
noOfSurprises = 0
reqdResult = 0
sCount = 0
reqdCount = 0
points = 0


for ln in objfile.readlines():
  if not num:
    num = int(ln.replace('\n', ''))
    continue
  counter +=1
  
  values = [int(i) for i in ln.replace('\n', '').split(' ')]
  noGooglers = values[0]
  noSurprises = values[1]
  reqdRes = values[2]
  scores = [values[3+i] for i in range(noGooglers)]

  for i in scores:
    points = i
    a = points /  3
    b = points %  3
    if (b == 0):
      if( a >= reqdRes):
        reqdCount += 1
      elif ((a + 1) >= reqdRes and sCount < noSurprises and points > 0):
        reqdCount += 1
        sCount += 1
    elif (b == 1):
      if( (a+1) >= reqdRes):
        reqdCount += 1
    elif (b == 2):
      if( (a+1) >= reqdRes):
        reqdCount += 1
      elif ((a + 2) >= reqdRes and (sCount < noSurprises)):
        reqdCount += 1
        sCount += 1
  output = reqdCount        
  result.append('Case #%s: %s' %(counter, output))
  output = ''
  values = []
  noGooglers = 0
  noSurprises = 0
  reqdRes = 0
  sCount = 0
  reqdCount = 0
  points = 0
  
objfile.close()
objfile = open('test.out', 'w')
objfile.write(string.join(result, '\n'))
objfile.close()
