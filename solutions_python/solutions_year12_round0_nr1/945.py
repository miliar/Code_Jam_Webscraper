#
import re
import math

f = open("A-small-attempt3.in","r")
fo = open("A-small.out","w")

s = 'y n f i c w l b k u o m x s e v z p d r j g t h a q'
t = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
#s ='ejp mysljylc kd kxveddknmc re jsicpdrysi'
#s = s + 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'
#s = s + 'de kr kd eoya kw aej tysr re ujdr lkgc jv'

#t ='our language is impossible to understand'
#t = t + 'there are twenty six factorial possibilities'
#t = t + 'so it is okay if you want to just give up'

dic = {}
for i in range(len(s)):
      dic[s[i]] = t[i]
#dic['z'] = 'h'
#dic['q'] = 'z'




lines = f.readlines()
lines = [l.strip() for l in lines]
nlines = len(lines)

i = 0
T = int(lines[i])
for icase in range(T):
      # set parameters
      i = i + 1
      ans = ''
      for c in lines[i]:
            ans = ans + dic[c]
      print("Case #",icase+1,": ",ans,sep="",file=fo)
      print("Case #",icase+1,": ",ans,sep="")


#print("Case #",icase+1,": ",nswitch,sep="",file=fo)
f.close()
fo.close()

