#!/usr/bin/python
import sys

keys = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
keys = list(keys)

values = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"
values = list(values)

dict = {}
junk = map(lambda k, v: dict.update({k: v}), keys, values)
dict['z'] = 'q'
dict['q'] = 'z'
number_of_cases = raw_input()

for x in range(1, int(number_of_cases) + 1): 
  first_string = list(raw_input())

  sys.stdout.write("Case #" + str(x) + ": ") 
  for x in first_string:
    if x != ' ':
      sys.stdout.write(dict[x])
    else:
      sys.stdout.write(' ')

  sys.stdout.write('\n') 
