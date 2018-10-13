from repr import repr
import math

def most_bit(num):
  return int(math.floor(math.log(num,2)))

def sumf(a,b):
  return a+b

def toInt(c):
  return int(c)
input  = open('../input/Q_2011_c.in')
CASES  = int(input.readline())
for case in range(CASES):
  input.readline()
  candies = map(toInt,input.readline().rstrip().split(' '))
  res = candies[0]
  for c in candies[1:]:
    res = res ^ c
  ans=0
  if not res:
    ans = sum(candies)-min(candies) 
    
  print 'Case #'+str(case+1)+': '+(not res and str(ans) or  'NO')
  