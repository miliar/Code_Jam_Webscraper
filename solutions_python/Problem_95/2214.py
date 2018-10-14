#!/usr/bin/env python

input_1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
input_2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
input_3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv"

output_1 = "our language is impossible to understand" 
output_2 = "there are twenty six factorial possibilities"
output_3 = "so it is okay if you want to just give up"

char_map = {'z': 'q', 'q': 'z'}

for c_in, c_out in zip((input_1+input_2+input_3) , (output_1 + output_2 + output_3)):
  char_map[c_in] = c_out

f = open('small.in')
T = int(f.readline())

for t in range(1,T+1):
  out = ''
  for c in f.readline().strip():
    out += char_map[c]
  print "Case #%i:"%t, out
