# Python 2.5.2
# GCJ 2012, Q, A

ct = ['ejp mysljylc kd kxveddknmc re jsicpdrysi',
'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
'de kr kd eoya kw aej tysr re ujdr lkgc jv',
'y qee']

pt = ['our language is impossible to understand',
'there are twenty six factorial possibilities',
'so it is okay if you want to just give up',
'a zoo']

tr = [-1 for i in range(26)]
for i in range(len(pt)):
    for x,y in zip(ct[i], pt[i]):
        if x != ' ':
            tr[ord(x)-ord('a')] = ord(y)-ord('a')

for i in range(26):
    if tr.count(i) == 0:
        tr[tr.index(-1)] = i

def enc(x):
    if x != ' ':
        x = tr[ord(x) - ord('a')]
        x = chr(x + ord('a'))
    return x

f = open("A-small-attempt0.in", "r")
L = f.read().split('\n');

f = open("A-small-attempt0.out.txt", "w")

n = int(L[0])
for i in range(n):
    s = L[i+1]
    s = ''.join(enc(x) for x in L[i+1])
    f.write("Case #%s: %s\n" % (i+1,s))
f.close()
    
