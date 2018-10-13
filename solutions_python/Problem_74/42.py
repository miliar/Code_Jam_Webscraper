import sys, os, re

T = int(sys.stdin.readline())

for case_ in range(T):
  sys.stdout.write('Case #{0}: '.format(case_ + 1))
  ss = sys.stdin.readline()[:-1].split(' ')[1:]
  commands = [(ss[2 * i], int(ss[2 * i + 1])) for i in range(len(ss) // 2)]

  O = 1
  B = 1
  To = 0
  Tb = 0

  for command in commands:
    if command[0] == 'O':
       To += max(1, abs(O - command[1]) + 1) 
       To = max(To, Tb + 1)
       O = command[1]
    else:
       Tb += max(1, abs(B - command[1]) + 1) 
       Tb = max(Tb, To + 1)
       B = command[1]
#    print('O = {0}, B = {1}, To = {2}, Tb = {3}'.format(O, B, To, Tb))


  print(max(To, Tb))

