#!/usr/bin/python

enc = []
org = []
enc.append("ejp mysljylc kd kxveddknmc re jsicpdrysi qz")
org.append("our language is impossible to understand zq")
enc.append("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd")
org.append("there are twenty six factorial possibilities")
enc.append("de kr kd eoya kw aej tysr re ujdr lkgc jv")
org.append("so it is okay if you want to just give up")

d = {}
for j in range(len(enc)):
  x = enc[j]
  y = org[j]
  for i in range(len(x)):
    if x[i]!=" ":
      d[x[i]]=y[i]

n = raw_input()
for i in range(int(n)):
  r = raw_input()
  res = ""
  for j in range(len(r)):
    if r[j]!=" ":
      res+=d[r[j]]
    else:
      res+=" "
  print "Case #%d:" % (i+1), res
