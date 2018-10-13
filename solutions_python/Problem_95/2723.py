
a = {'a': 'y', 'o': 'e', 'z': 'q', 'q': 'z'}
cache = {}
mapping_text = {'ejp mysljylc kd kxveddknmc re jsicpdrysi': 'our language is impossible to understand',
                'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd': 'there are twenty six factorial possibilities',
                'de kr kd eoya kw aej tysr re ujdr lkgc jv': 'so it is okay if you want to just give up'}

for coded, plain in mapping_text.items():
    for i in xrange(len(coded)):
        a[coded[i]] = plain[i]

#for l in sorted(a.keys()):
    #print l

def decode(text):
    return ''.join([a[letter] for letter in text])

for i, line in enumerate(open('A-small-attempt0.in').readlines()):
    if i > 0:
        print 'Case #'+str(i)+': '+decode(line.strip())


