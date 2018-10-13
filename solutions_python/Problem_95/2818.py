import re

input_ = '''ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jvq'''

output = '''our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give upz'''

alfa = 'abcdefghijklmnopqrstuvwxyz'

translate = dict()
i = 0
for i in xrange(len(input_)):
    if input_[i] not in translate.keys():
        translate[input_[i]] = output[i]

missingi = [ i for i in alfa if i not in translate.keys() ]
missingo = [ i for i in alfa if i not in translate.values() ]

if len(missingi) == 1 and len(missingo) == 1:
    translate[missingi[0]] = missingo[0]

for T in xrange(1, int(raw_input())+1):
    print "Case #%i: %s" % (T, "".join([ translate[ci] for ci in raw_input() ]))
