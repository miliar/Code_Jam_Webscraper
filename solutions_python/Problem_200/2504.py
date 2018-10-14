

def isTidy(number):
  prevNumber = 0
  for digit in list(number):
    if int(digit) < prevNumber:
      return False
    prevNumber = int(digit)
  return True


def decrement(number):
  prevNumber = 9
  newNumber = []
  for digit in reversed(list(number)):
    if int(digit) > prevNumber:
      newNumber = ['9' for i in list(newNumber)]
      new_digit = int(digit)-1
      newNumber.append(str(new_digit))
      prevNumber = new_digit
    else:
      newNumber.append(digit)
      prevNumber = int(digit)
  if newNumber[-1] == '0':
    newNumber = newNumber[:-1]
  return ''.join(reversed(newNumber))


def getLastTidy(number):
  while(1):
    if isTidy(number):
      return number
    number = decrement(number)
  return None


t = int(raw_input())
for i in xrange(1, t + 1):
  n = raw_input()
  result = decrement(n);
  print "Case #{}: {}".format(i, result)



