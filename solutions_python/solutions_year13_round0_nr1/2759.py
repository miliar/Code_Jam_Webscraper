import sys
import math

def value(a):
  if a == 'X':
    return 100
  elif a == 'O':
    return -100
  elif a == 'T':
    return 0
  else :
    return 1

def print_res(res, case):
  for cnt in res:
    if cnt == 300 or cnt == 400:
      out.write('Case #' + str(case) + ': X won \n')
      return 0
    if cnt == -300 or cnt == -400:
      out.write('Case #' + str(case) + ': O won \n')
      return 0

  for cnt in res:
    if cnt%100 != 0:
       break
    else :
      out.write('Case #' + str(case) + ': Draw \n')
      return 0

  out.write('Case #' + str(case) + ': Game has not completed \n')


out = open('output_tiktak.txt', 'w')

case = 0

tab = {}

f = open(sys.argv[1], 'r')
T = f.readline()
print T

for i in range (1, int(T)+1):
  res = set()
  for j in range (0,4):
    tab[j] = list(f.readline())
    tab[j].remove(tab[j][-1])

    cnt = 0
    for i in tab[j]:
      cnt += value(i) 
    res.add(cnt)

  for j in range (0,4):
    cnt = 0
    for l in range (0,4):
      cnt += value(tab[l][j])
    res.add(cnt)

  cnt = 0
  for j in range (0,4):
    cnt += value(tab[j][j])
  res.add(cnt)

  cnt = 0
  cnt += value(tab[0][3])
  cnt += value(tab[1][2])
  cnt += value(tab[2][1])
  cnt += value(tab[3][0])
  res.add(cnt)

  f.readline()
  #print res
  case += 1
  print_res(res,case)

out.close()

