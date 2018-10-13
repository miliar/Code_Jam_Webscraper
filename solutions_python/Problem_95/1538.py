a = 'ejp mysljylc kd kxveddknmc re jsicpdrysi'
a1 = 'our language is impossible to understand'
b = 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'
b1 = 'there are twenty six factorial possibilities'
c = 'de kr kd eoya kw aej tysr re ujdr lkgc jv'
c1 = 'so it is okay if you want to just give up'

d = {}
for i in range(len(a)):
    if(a[i] not in d):
        d[a[i]] = a1[i]
for i in range(len(b)):
    if(b[i] not in d):
        d[b[i]] = b1[i]
for i in range(len(c)):
    if(c[i] not in d):
        d[c[i]] = c1[i]

d['z'] = 'q'
d['q'] = 'z'



infile = open('infile.txt','r')
outfile = open('outfile.txt','w')
n = int(infile.readline())

for i in range(1, n+1):
    inline = infile.readline()[:-1]
    outline = ''
    for l in inline:
        outline += d[l]
    outfile.write('Case #' + str(i) + ": " + outline + "\n")

outfile.close()
infile.close()
