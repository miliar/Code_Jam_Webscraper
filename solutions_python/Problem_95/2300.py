#!/usr/bin/python
import sys;
d=dict();
s1="""ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv"""
s2="""our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up"""
for i in range(len(s1)):
  d[s1[i]]=s2[i]
d["q"]="z"
d["z"]="q"
#print len(d)
for i in "abcdefghijklmnopqrstuvwxyz":
  if d.has_key(i):
	pass
  else:
	print i
i=0;
nin=input()
for j in range(nin):
  x=raw_input()
  sys.stdout.write("Case #"+str(j+1)+": ");
  #print "Case #",j+1," :",
  for k in x:
    sys.stdout.write(d[k]);
  print ;
  
  
