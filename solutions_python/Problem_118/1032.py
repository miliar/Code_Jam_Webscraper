
import sys, math

f = file('C-small-attempt0.in')

def is_p(s):
  if len(s) == 1:
    return True
  for i in range(len(s)):
    if s[i] != s[len(s) - i - 1]:
      return False
  return True

def c_p(a, b):
  r = 0
  for i in range(int(math.sqrt(a)), int(math.sqrt(b)) + 1):
    i2 = i*i
    if (is_p(str(i)) and is_p(str(i2))) and i2 >= a and i2 <= b:
      #print i, i*i
      r = r + 1
  return r

#print c_p(1, 100000000000000)

f.readline()

i = 1
for line in f:
  a, b = map(int, line.split())
  print 'Case #' + str(i) + ': ' + str(c_p(a, b)) 
  i += 1

