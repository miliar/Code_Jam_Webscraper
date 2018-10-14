#! /usr/bin/env python

import sys,copy

f_in = open(sys.argv[1], 'r')
f_out = open('%s.out' % sys.argv[1], 'w')
num_cases = int(f_in.readline())
i = 1
#zero = False
while i <= num_cases:
  zero = False
  dict = {'a':[], 'c':[], 'd':[], 'e':[], 'j':[], 'l':[],\
                  'm':[], 'o':[], 't':[], 'w':[], ' ':[]}
  str = f_in.readline()
  str = list(str)
  for j in range(len(str)):
    if str[j] in dict:
      dict[str[j]].append([j,0])
  arr = list('welcome to code jam')
  for j in range(len(arr)):
    arr[j] = copy.deepcopy(dict[arr[j]])
    if len(arr[j]) == 0:
      zero = True
      break
  if not zero:
    j = len(arr) - 1
    for k in range(len(arr[j])):
      arr[j][k][1] = 1
    j -= 1
    while j >= 0:
      k = len(arr[j]) - 1
      m = len(arr[j+1]) - 1
      while k >= 0:
        if m < 0 or arr[j+1][m][0] < arr[j][k][0]:
          k -= 1
          if k >= 0:
            arr[j][k][1] = arr[j][k+1][1]
        else:
          arr[j][k][1] += arr[j+1][m][1]
          m -= 1
        arr[j][k][1] = arr[j][k][1] % 10000
      if arr[j][0][1] == 0:
        zero = True
        break
      j -= 1
  total = 0
  if not zero:
    for k in range(len(arr[0])):
      total += arr[0][k][1]
  f_out.write('Case #%d: %04d\n' % (i, total))
  print 'Case #%d: %04d' % (i, total)
  i += 1
f_in.close()
f_out.close()
