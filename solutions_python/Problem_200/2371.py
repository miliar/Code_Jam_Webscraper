#3 solution
#1. 144132  decrease the digit that outly
#   144
#   1(2)   add 9 to remaining
#2. if %10 then -1 
#   320 -1 = 319

def factorTen(n):
  if (n%10==0):
    n = n-1
  return n

def getfirstIndex(n):
  number = str(n)
  maxval = number[0]
  index = 0
  for i in range((len(number)-1)):
    if number[i] > maxval:
      maxval = number[i]
      index = i
    if number[i] > number[i+1]:
      return index
  return -1

def changeNum(n, index):
  number = str(n)
  newnum = int(number[index])-1
  nine = "9" * (len(number[index:])-1)
  number = number[:index] + str(newnum) + nine
  return int(number)
    

#print changeNum(14331, 1)


def calculate(number):
  if number<10:
    return number
  number = factorTen(number)
  index = getfirstIndex(number)
  if index > -1:
    number = changeNum(number, index )
  return number
  
tests = input("")
#print tests
for test in range(tests):
  number= int(raw_input())
  print "Case #" + str(test+1) +": "+str(calculate(number))
