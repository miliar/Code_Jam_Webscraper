import re

f = open('c:\users\carlos\google\A-large.in','r')
lines = f.readlines()
f.close()
for i in range(len(lines)):
    lines[i] = lines[i].strip('\n')
l,d,n = lines[0].rsplit(' ',3)
l = int(l)
d = int(d)
n = int(n)

words = lines[1:1+d]
patterns = lines[1+d:1+d+1+n]


cases = [0] * len(patterns)
for i in range(len(patterns)):
    patterns[i] = patterns[i].replace('(','[').replace(')',']')
    ex = re.compile(patterns[i])
    for w in words:
        if ex.search(w):
            cases[i] = cases[i] + 1

f = open('c:\users\carlos\google\output-a-large.out','w')
for i in range(len(cases)):
    f.write('Case #%i: %i\n' %(i+1, cases[i]))
f.close()

print 'Length: %s' % l
print '%s words' % d
print words
print '%s patterns' % n
print patterns
print 'Resultado'
print cases
