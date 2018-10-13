import sys

d = {}

a = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh\n wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv"
b = "our language is impossible to understandthere are twenty six\n factorial possibilitiesso it is okay if you want to just give up"

for (x,y) in zip(list(a),list(b)):
  d[x] = y
d['q'] = 'z';
d['z'] = 'q';

for i,l in enumerate(sys.stdin.readlines()[1:]):
  print 'Case #%d:' %(i+1,),''.join(map(lambda x:d[x], l)),

