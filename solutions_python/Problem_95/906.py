#!/usr/bin/python
import sys
import operator
from operator import itemgetter
data = ["ejp mysljylc kd kxveddknmc re jsicpdrysi","rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd","de kr kd eoya kw aej tysr re ujdr lkgc jv"]
if len(sys.argv)>1:
  infi = sys.argv[1]
  data = []
  fi = open(infi)
  lines = fi.readlines()
  d = 0
  for line in lines:
    if d!=0:
      line = line.replace("\n","")
      data.append(line)
    d+=1
fre = ['e','t','a','o','i','n','s','h','r','d','l','c','u','m','w','f','g','y','p','b','v','k','j','x','q','z']

keys = {' ':0, 'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'p':0,'q':'z','r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':'q'}
cpare = ["ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv","our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"]
for i in range(len(cpare[0])):
  keys[cpare[0][i]]=cpare[1][i]
c=1
for i in data:
  output = map(lambda x:keys[x],i)
  print "Case #"+str(c)+": "+''.join(output)
  c+=1
