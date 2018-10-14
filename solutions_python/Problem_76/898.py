import sys
import re


def calculate(num, dataset):
  sumDict = {}

  for i in xrange(num-1):
    sumDict[i] = []
    if i == 0:
      sumDict[i].append([0])
    else:
      for j in xrange(len(sumDict[i-1])):
        for k in xrange(num - sumDict[i-1][j][i-1] - 1):
          templist = []
          templist.extend(sumDict[i-1][j])
          templist.append(k + sumDict[i-1][j][i-1] + 1)
          sumDict[i].append(templist)
  max = 0
  for i in xrange(len(sumDict)):
    for line in sumDict[i]:
      sumA=0
      sumB=0
      unicSumA = 0
      unicSumB = 0
      for j in xrange(num):
        if j in line:
          sumA = sumA^int(dataset[j])
          unicSumA = unicSumA + int(dataset[j])
        else:
          sumB = sumB^int(dataset[j])
          unicSumB = unicSumB + int(dataset[j])
      if sumA == sumB:
        if max < unicSumA:
          max = unicSumA
        if max < unicSumB:
          max = unicSumB
  return max

if __name__ == '__main__':                                                  
  if len(sys.argv) < 2:                                                     
    raise "please file name"                                                
  r = re.compile('[\ \n]')                                                  
  try:                                                                      
     fi = open(sys.argv[1], "r")
     lineNum = fi.readline()
     if lineNum > 0:
       for i in xrange(int(lineNum)):
         candyNum = int(fi.readline())
         line = fi.readline()
         dataset =  r.split(line) 
         result = calculate(candyNum, dataset)
         if result == 0:
           print "Case #%d: NO" % (i+1)
         else:
           print "Case #%d: %d" % (i+1, result)
  except IOError, inst:
    print inst 
  finally:
    if fi: fi.close()
