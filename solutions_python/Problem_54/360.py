#!/usr/bin/python

import fractions

fi = open("./B-large.in", "r")
fo = open("./B-large.out", "w")

C = int(fi.readline())

for count in xrange(C):
  tests = fi.readline().split()
##  print(tests)
  if int(tests[0]) == 2:
    a1 = abs(int(tests[1]) - int(tests[2]))
    if(int(tests[1]) % a1 == 0):
      a2 = 0
    else:
      a2 = a1 - (int(tests[1]) % a1)
    print("Case #%d: %d\n" % (int(count)+1, a2))
    fo.writelines("Case #%d: %d\n" % (int(count)+1, a2))
  else:
    base_num = abs(int(tests[1]) - int(tests[2]))
    a2 = 0
    for cc in xrange(int(tests[0])-2):
      a1 = abs(int(tests[cc+2]) - int(tests[cc+3]))
      if a1 == 0: continue
      base_num = fractions.gcd(base_num, a1)
      if base_num == 0:
        a2 = 0
      elif (int(tests[1]) % base_num) == 0:
        a2 = 0
      else:
        a2 = base_num - (int(tests[1]) % base_num)
    print("Case #%d: %d\n" % (int(count)+1, a2))
    fo.writelines("Case #%d: %d\n" % (int(count)+1, a2))

fi.close
fo.close
