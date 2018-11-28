# Speaking in Tongues

import sys

def getline():
    return sys.stdin.readline().strip()

    

n = int(getline())

mapsrc = { 
    'ejp mysljylc kd kxveddknmc re jsicpdrysi' : 'our language is impossible to understand',
    'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd' : 'there are twenty six factorial possibilities',
    'de kr kd eoya kw aej tysr re ujdr lkgc jv' : 'so it is okay if you want to just give up',
};


set1 = set()
set2 = set()
for chi in range(26):
    ch = chr( ord('a') + chi )
    set1.add(ch)
    set2.add(ch)

mapping = {' ' : ' '}
for k in mapsrc:
    v = mapsrc[k]
    for i in range(len(k)):
        if k[i] in mapping and mapping[k[i]] != v[i]:
            print 'error mapping %s:%s' % (k[i], v[i])
        mapping[k[i]] = v[i]
        if k[i] in set1:
            set1.remove(k[i])
        if v[i] in set2:
            set2.remove(v[i])

#for k in set1:
#    for v in set2:
#        mapping[k] = v
mapping['q'] = 'z'
mapping['z'] = 'q'

for id in range(1, n+1):
    print 'Case #%d:' % id,
    
    str = ''
    for ch in getline():
        str += mapping[ch]
    
    print str
    
