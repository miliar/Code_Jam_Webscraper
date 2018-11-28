import sys

myin = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
myout = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"

trans = {}

for j in range(len(myin)):
  trans[myin[j]] = myout[j]

trans['z']='q'
trans['q']='z'

N = input()

for i in range(N):
  print ('Case #%s: '%(i+1)) + ''.join(map((lambda j: trans[j]), raw_input()))
