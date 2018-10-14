import sys, os, operator

d = {}
str = 'ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv'
str2 = 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up'

for i in xrange(0,len(str)):
    d[str[i]]=str2[i]
#d['z']='q'
d['q']='z'
d['z']='q'


#f = open("sample-in.txt")
f = sys.stdin

#print d
#print sorted(d)
#print sorted(d.values())

cases = f.readline()
for case in xrange(1,int(cases)+1):
    sen = f.readline().strip()
    print 'Case #%d: %s'%(case, ''.join([d[c] for c in sen]))

