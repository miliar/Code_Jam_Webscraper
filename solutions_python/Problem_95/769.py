# -*- coding: utf-8 -*-
import sys
from string import maketrans

google = '''ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jvqz'''

english = '''our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give upzq'''

trantab = maketrans(google, english)


with open('A-small-attempt1.in', 'r') as si, open('A-small-attempt1.out', 'w') as so:
    num = int(si.readline())
    result = ''
    for i in range(num):
        g = si.readline()
        result = result + 'Case #' + str(i+1) + ': ' + g.translate(trantab)
    print result
    so.write(result)