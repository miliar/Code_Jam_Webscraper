import sys
dict = {'y': 'a', 'e':'o', 'q': 'z'}
text1 = 'ejp mysljylc kd kxveddknmc re jsicpdrysi'
text2 = 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'
text3 = 'de kr kd eoya kw aej tysr re ujdr lkgc jv'
translation1='our language is impossible to understand'
translation2='there are twenty six factorial possibilities'
translation3='so it is okay if you want to just give up'
for i in xrange(len(text1)):
    if text1[i] not in dict:
        dict[text1[i]] = translation1[i]
for i in xrange(len(text1)):
    if text2[i] not in dict:
        dict[text2[i]] = translation2[i]
for i in xrange(len(text1)):
    if text3[i] not in dict:
        dict[text3[i]] = translation3[i]
letters = set(map(chr,xrange(97,97+26))+[' '])
dict[list(letters-set(dict.keys()))[0]] = list(letters-set(dict.values()))[0]

fh = open(sys.argv[1])
T = int( fh.readline() )
for i in xrange(T):
    trans = ''.join([dict[l] for l in fh.readline().rstrip("\n")])
    print "Case #{0}: {1}".format(i+1, trans)
fh.close()
