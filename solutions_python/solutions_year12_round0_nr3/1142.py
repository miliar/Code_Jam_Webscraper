#!/usr/bin/python4

def RecycledNumbers():
  minLim = long(values[0])
  maxLim = long(values[1])
  if maxLim <= 10:
    return 0
  intCount = 0
  comb = {}
  temp = ''
  tempDigit = 0
  for i in range(minLim, maxLim+1):
    temp = str(i)
    for k in range(1, len(temp)):
      tempDigit = temp[-k:] + temp[0:len(temp)-k]
      if int(tempDigit[0]) == 0:
        continue
      if int(temp) == int(tempDigit):
        continue
      if int(tempDigit) in comb.keys():
        continue
      if int(tempDigit) in comb.values():
        continue
      if int(tempDigit) in range(minLim, maxLim+1):
        comb[int(temp)] = int(tempDigit)
        intCount += 1
      
    
  return intCount


import string
fname = 'small'
objfile = open('%s.in' % fname, 'r')
result = []
output = ''
num = 0
counter = 0

for ln in objfile.readlines():
  if not num:
    num = long(ln.replace('\n', ''))
    continue
  counter +=1
  
  values = [i for i in ln.replace('\n', '').split(' ')]
  output = RecycledNumbers()       
  result.append('Case #%s: %s' %(counter, output))
  output = ''
  values = []
 
  
objfile.close()
objfile = open('test.out', 'w')
objfile.write(string.join(result, '\n'))
objfile.close()
