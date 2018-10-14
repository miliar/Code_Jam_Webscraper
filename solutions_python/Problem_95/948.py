#!/usr/bin/env python
import math

input1 = "our language is impossible to understand"
input2 = "there are twenty six factorial possibilities"
input3 = "so it is okay if you want to just give up"

output1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
output2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
output3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv"

cipher = {}
for x in range(len(output1)):
    cipher[output1[x]] = input1[x];
for x in range(len(output2)):
    cipher[output2[x]] = input2[x];
for x in range(len(output3)):
    cipher[output3[x]] = input3[x];
cipher['q'] = 'z'
cipher['z'] = 'q'

N = int(raw_input())
for t in range(1,N+1):
    enc = str(raw_input())
    dec = ''
    for x in range(len(enc)):
        dec = dec + cipher[enc[x]]
    print 'Case #'+str(t)+':',dec

