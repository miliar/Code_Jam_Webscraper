import sys
from math import sqrt
def pal(n):
  if type(n) is not int:
    return False
  length = len(str(n))
  if length == 1:
    return True
  num = str(n)
  l_num = num[:(length/2)]
  if length%2 == 0:
    r_num = num[length/2:]
  else:
    r_num = num[(length/2)+1:]
  rhs = [x for x in r_num]
  rhs.reverse()
  rhs = "".join(rhs)
  if l_num == rhs:
    return True
  return False

def checkpal(n, num2):
  if pal(n):
    if int(sqrt(n)*10)%10 == 0:
      n = int(sqrt(n))
      if pal(n):
        return True
  return False
def cutBush(lis):
  num1 = int(lis[0])
  num2 = int(lis[1])
  counter = 0
  for number in xrange(num1, num2+1):
    if checkpal(number, num2+1):
      counter = counter+1
  return counter

if __name__ == '__main__':
  fileHandle = open(sys.argv[1])
  lines = fileHandle.readlines()
  j = 0
  totallines = int(lines[0].rstrip())
  for i in range(totallines):
			j = i+1;
			nums = lines[j].rstrip()
#			dictionay[int(lines[i])] = lines[i-1].split(' ')
#			print lines[i],'\n\n',lines[i+1]
			print 'Case #%s: %s' % (j, cutBush(nums.split(' ')))

