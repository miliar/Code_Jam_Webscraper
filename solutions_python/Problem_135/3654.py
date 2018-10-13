import string
import re

print "**Code jam 2014 Problem 1**"

foo = raw_input('Enter file name: ')
f = open(foo,'r')
data = f.readlines()
f.close()
g = open('out.txt', 'w')
print "Number of lines: " + str(int(data[0]))

numlines = int(data.pop(0))
cnt = 0
for i in range(numlines):
  fc = str(data[cnt+0].rstrip())
  sc = str(data[cnt+5].rstrip())
  f_list = []
  f_list.append(data[cnt+1].rstrip().split())
  f_list.append(data[cnt+2].rstrip().split())
  f_list.append(data[cnt+3].rstrip().split())
  f_list.append(data[cnt+4].rstrip().split())
  s_list = []
  s_list.append(data[cnt+6].rstrip().split())
  s_list.append(data[cnt+7].rstrip().split())
  s_list.append(data[cnt+8].rstrip().split())
  s_list.append(data[cnt+9].rstrip().split())
  cnt+=10
  comp1 = f_list[int(fc)-1]
  comp2 = s_list[int(sc)-1]
  chk = 0
  num = 0
  for comp1c in comp1:
    if comp1c in comp2:
      num = comp1c
      chk += 1
  if chk == 0:
    g.write('Case #' + str(i+1) + ': ' + 'Volunteer cheated!\n')
  elif chk == 1:
    g.write('Case #' + str(i+1) + ': ' + str(num) + '\n')
  elif chk > 1:
    g.write('Case #' + str(i+1) + ': ' + 'Bad magician!\n')

