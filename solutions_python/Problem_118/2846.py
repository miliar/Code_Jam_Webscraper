import sys
import math

out = open('output.txt', 'w')

def is_square(n):
    r = math.sqrt(n)
    return int(r) if int(r + 0.5) ** 2 == n else 0 

def is_pal(n):
  s = str(n)
  el = list(s)
  while len(el) > 1:
    if el[0] == el[-1]:
      el.remove(el[0])
      el.remove(el[-1])
    else :
      return False
  return True

case = 0

f = open(sys.argv[1], 'r')
T = f.readline()
for a in f:
  case += 1
  cnt = 0
  print a
  A, B = a.split(' ')
  print A, B
  if int(B) < int(A):
     out.write('Case #' + str(case) + ' : 0\n')
     continue
  for i in range(int(A),int(B) + 1):
    a = is_square(i)
    if a != 0:
      if is_pal(a) and is_pal(i):
        cnt +=1
  out.write('Case #' + str(case) + ': ' + str(cnt) + '\n')

out.close()

