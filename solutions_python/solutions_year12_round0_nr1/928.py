from string import maketrans

a = 'ejp mysljylc kd kxveddknmc re jsicpdrysi'
b = 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'
c = 'de kr kd eoya kw aej tysr re ujdr lkgc jv'
x = 'our language is impossible to understand'
y = 'there are twenty six factorial possibilities'
z = 'so it is okay if you want to just give up'

d = {'q':'z', 'z':'q'}
for i in range(len(a)):
    d[a[i]] = x[i]
for i in range(len(b)):
    d[b[i]] = y[i]
for i in range(len(c)):
    d[c[i]] = z[i]

f = ''
t = ''
for i in range(26):
    f += chr(ord('a')+i)
    t += d[f[i]]
trans = maketrans(f, t)

infile = open('a.in', 'r')
outfile = open('a.out', 'w')
    
n = int(infile.readline())
for i in range(n):
    s = infile.readline()
    outfile.write('Case #{0}: {1}'.format(i+1, s.translate(trans)))
infile.close()
outfile.close()
