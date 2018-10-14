
f = open('/home/ronan/Downloads/A-small-attempt1.in', 'r')
lines = map(lambda e : e.strip('\n'),f.readlines())

i, lines = int(lines[0]), lines[1:]

original = 'ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv'
translated = 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up'
map = {'z' : 'q',
       'o' : 'e',
       'a' : 'y',
       'q' : 'z'}
for o, t in zip(original,translated):
    map[o] = t

for line in range(0,i):
    translated = ''
    for letter in lines[line]:
        translated = translated + (' ' if letter == ' ' else map[letter])
    print 'Case #%s: %s' % (int(line)+1, translated)
