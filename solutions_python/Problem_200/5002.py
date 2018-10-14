import sys


def findTidy(number):
  tidyList = [];
  while number >= 10:
    tidyList.append(number%10)
    number = number/10
  tidyList.append(number)
  
  if tidyList[len(tidyList)-1] > tidyList[len(tidyList)-2]:
    for i in range(0,len(tidyList)-1):
      tidyList[i] = 9
    tidyList[len(tidyList)-1] = tidyList[len(tidyList)-1] - 1
    return tidyList
  
  for i in range(0, len(tidyList)-1):
    if(tidyList[i] < tidyList[i+1]):
      tidyList[i] = 9
      tidyList[i+1] = tidyList[i+1] - 1
    elif(tidyList[i] == 0 and tidyList[i] == tidyList[i+1]):
      tidyList[i] = 9
  return tidyList
      
def formNumber(tidyList):
  i = 1
  tidyNumber = 0
  for j in range(0, len(tidyList)):
    tidyNumber = tidyNumber + (i*tidyList[j])
    i = i * 10
  return tidyNumber

def checkTidy(tidyList):
  for i in range(0, len(tidyList)-1):
    if tidyList[i] >= tidyList[i+1]:
      continue
    else:
      return False
  return True
  
def getTidyNumber(number):
  tidyList = findTidy(number)
  while not checkTidy(tidyList):
    tidyList = findTidy(formNumber(tidyList))
  return formNumber(tidyList)
  

t = int(raw_input())  # read a line with a single integer
for i in xrange(0, t):
  n= long(raw_input())  # read a list of integers, 2 in this case
  print "Case #{}: {}".format(i, getTidyNumber(n))
