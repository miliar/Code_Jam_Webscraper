def f(a, b):
  for x,y in zip(a,b):
    d[x] = y


d={}

f('y qee', 'a zoo')
f('ejp mysljylc kd kxveddknmc re jsicpdrysi', 'our language is impossible to understand')
f('rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd', 'there are twenty six factorial possibilities')
f('de kr kd eoya kw aej tysr re ujdr lkgc jv', 'so it is okay if you want to just give up')
f('z', 'q')



#print len(d), sorted(d)
c=0
for l in open('A-small-attempt0.in'):
    if c > 0:
      t=''
    
      for i in l.strip():
        t += d[i]
      print 'Case #' + str(c) + ': ' + t
    c += 1
       